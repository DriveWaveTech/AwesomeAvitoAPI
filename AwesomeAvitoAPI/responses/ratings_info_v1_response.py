import pydantic


class Rating(pydantic.BaseModel):
    reviewsCount: int
    reviewsWithScoreCount: int
    score: float


class RatingsInfoV1Response(pydantic.BaseModel):
    isEnabled: bool
    rating: Rating
