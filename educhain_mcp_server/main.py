from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import List, Dict, Union
import json
import logging
from educhain_utils import EduChainContentGenerator # Our simulated educhain functions

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(
    title="EduChain MCP Server",
    description="MCP server integrating EduChain for educational content generation.",
    version="1.0.0"
)

# Initialize EduChain content generator
# You can pass an LLM instance here if you've configured it in educhain_utils.py
# edu_generator = EduChainContentGenerator(llm=...)
edu_generator = EduChainContentGenerator() 

class ToolDefinition(BaseModel):
    """Schema for defining an MCP tool."""
    name: str = Field(..., description="The unique name of the tool.")
    description: str = Field(..., description="A brief description of what the tool does.")
    parameters: Dict = Field(..., description="JSON schema for the tool's input parameters.")
    endpoint: str = Field(..., description="The API endpoint to call this tool.")
    method: str = Field("POST", description="The HTTP method for the tool's endpoint (e.g., GET, POST).")

class ResourceDefinition(BaseModel):
    """Schema for defining an MCP resource."""
    name: str = Field(..., description="The unique name of the resource.")
    description: str = Field(..., description="A brief description of the resource.")
    endpoint: str = Field(..., description="The API endpoint to access this resource.")
    method: str = Field("GET", description="The HTTP method for the resource's endpoint (e.g., GET, POST).")
    parameters: Dict = Field(None, description="Optional JSON schema for resource query parameters.")  # type: ignore

@app.get("/.well-known/mcp/tools", response_model=List[ToolDefinition])
async def get_mcp_tools():
    """
    Exposes the list of available MCP tools.
    """
    logging.info("Request received for /mcp/tools")
    tools = [
        ToolDefinition(
            name="generate_mcqs",
            description="Generates multiple-choice questions for a given topic.",
            parameters={
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "description": "The educational topic for the MCQs."},
                    "num_questions": {"type": "integer", "description": "Number of MCQs to generate (default: 5).", "default": 5}
                },
                "required": ["topic"]
            },
            endpoint="/tools/generate_mcqs"
        ), # type: ignore
        ToolDefinition(
            name="generate_flashcards",
            description="Generates flashcards (front/back) for a given topic. (Bonus)",
            parameters={
                "type": "object",
                "properties": {
                    "topic": {"type": "string", "description": "The educational topic for the flashcards."},
                    "num_cards": {"type": "integer", "description": "Number of flashcards to generate (default: 5).", "default": 5}
                },
                "required": ["topic"]
            },
            endpoint="/tools/generate_flashcards"
        ) # type: ignore
    ]
    return tools

@app.get("/.well-known/mcp/resources", response_model=List[ResourceDefinition])
async def get_mcp_resources():
    """
    Exposes the list of available MCP resources.
    """
    logging.info("Request received for /mcp/resources")
    resources = [
        ResourceDefinition(
            name="lesson_plan",
            description="Returns a lesson plan for a user-specified subject.",
            endpoint="/resources/lesson_plan",
            method="GET", 
            parameters={
                "type": "object",
                "properties": {
                    "subject": {"type": "string", "description": "The subject for which to generate a lesson plan."}
                },
                "required": ["subject"]
            }
        )
    ]
    return resources

# API ENDPOINTS FOR TOOLS

class GenerateMCQsRequest(BaseModel):
    topic: str
    num_questions: int = 5

@app.post("/tools/generate_mcqs")
async def generate_mcqs_endpoint(request: GenerateMCQsRequest):
    """
    API endpoint to generate multiple-choice questions using EduChain.
    """
    logging.info(f"Received request to generate MCQs for topic: {request.topic}, num_questions: {request.num_questions}")
    try:
        mcqs = edu_generator.generate_mcqs(request.topic, request.num_questions) # type: ignore
        return JSONResponse(content={"mcqs": mcqs}, status_code=status.HTTP_200_OK)
    except Exception as e:
        logging.error(f"Error generating MCQs: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate MCQs: {str(e)}"
        )

class GenerateFlashcardsRequest(BaseModel):
    topic: str
    num_cards: int = 5

@app.post("/tools/generate_flashcards")
async def generate_flashcards_endpoint(request: GenerateFlashcardsRequest):
    """
    API endpoint to generate flashcards using EduChain (Bonus).
    """
    logging.info(f"Received request to generate flashcards for topic: {request.topic}, num_cards: {request.num_cards}")
    try:
        flashcards = edu_generator.generate_flashcards(request.topic, request.num_cards) # type: ignore
        return JSONResponse(content={"flashcards": flashcards}, status_code=status.HTTP_200_OK)
    except Exception as e:
        logging.error(f"Error generating flashcards: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate flashcards: {str(e)}"
        )

#  API ENDPOINTS FOR RESOURCES

@app.get("/resources/lesson_plan")
async def get_lesson_plan_endpoint(subject: str):
    """
    API endpoint to retrieve a lesson plan for a given subject using EduChain.
    """
    logging.info(f"Received request for lesson plan for subject: {subject}")
    if not subject:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Subject parameter is required for lesson plan."
        )
    try:
        lesson_plan = edu_generator.generate_lesson_plan(subject) # type: ignore
        return JSONResponse(content={"lesson_plan": lesson_plan}, status_code=status.HTTP_200_OK)
    except Exception as e:
        logging.error(f"Error generating lesson plan: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to generate lesson plan: {str(e)}"
        )

@app.get("/")
async def root():
    return {"message": "EduChain MCP Server is running!"}