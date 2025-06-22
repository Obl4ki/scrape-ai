from typing import final
from sqlalchemy import String, create_engine


from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


engine = create_engine("sqlite:///scrape-ai.db")


class Base(DeclarativeBase):
    pass


@final
class ScrapedSite(Base):
    __tablename__ = "scraped_sites"

    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(255), unique=True)
    page_raw_content: Mapped[str] = mapped_column(String())


Base.metadata.create_all(engine)


def get_engine():
    """Get the SQLAlchemy engine."""
    return engine


def get_session():
    """Get a new SQLAlchemy session."""
    from sqlalchemy.orm import sessionmaker

    Session = sessionmaker(bind=engine)
    return Session()


def create_scraped_site(url: str, page_raw_content: str):
    """Create a new scraped site entry."""
    session = get_session()
    new_site = ScrapedSite(url=url, page_raw_content=page_raw_content)
    session.add(new_site)
    session.commit()
    session.close()
