import asyncio
import pytest
import logging

from uuid import UUID, uuid4
from pydantic.dataclasses import dataclass

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


@dataclass
class Input:
    title: str
    slug: str
    author: UUID
    category: UUID
    image: str | None = None

pytestmark = pytest.mark.asyncio

TIME = 10

async def test_create_a_author():
    input = Input(
            title="Uma publicação",
            slug="uma-publicação",
            author=uuid4(),
            category=uuid4(),
        )
    logger.debug("Antes create_author")
    await asyncio.sleep(TIME)
    logger.debug("Depois create_author")
    # create_publication = CreatePublication()
    # create_publication.execute(input)

async def test_create_a_publication():
    input = Input(
            title="Uma publicação",
            slug="uma-publicação",
            author=uuid4(),
            category=uuid4(),
        )
    logger.debug("Antes create_publication")
    await asyncio.sleep(TIME)
    logger.debug("Depois create_publication")
    # create_publication = CreatePublication()
    # create_publication.execute(input)
