from pydantic import BaseModel, validator


class Vote(BaseModel):
    user_id: int
    vote: int

    @validator("vote")
    def vote_must_be_in_range_1_to_5(cls, value):
        if value not in [1, 2, 3, 4, 5]:
            raise ValueError("Allowed vote values are 1,2,3,4,5")
        return value
