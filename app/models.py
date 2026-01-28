from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Snippet(Base):
    __tablename__ = "snippets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    language = Column(String)
    code = Column(Text)
    tags = Column(String, default="")

    @property
    def tag_list(self):
        if not self.tags:
            return []
        return [y for y in (t.strip() for t in self.tags.split(',')) if y]
