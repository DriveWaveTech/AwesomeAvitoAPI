import typing

from AwesomeAvitoAPI.base import AvitoBase

from AwesomeAvitoAPI.responses import CreateReviewAnswerV1, RatingsInfoV1Response, ReviewsV1Response


class AvitoRatings(AvitoBase):
    async def create_review_answer_v1(
        self,
        review_id: int,
        message: str
    ) -> CreateReviewAnswerV1:
        """
        https://developers.avito.ru/api-catalog/ratings/documentation#operation/createReviewAnswerV1

        :return:
        """
        if not isinstance(review_id, int):
            raise TypeError("review_id must be an integer")

        if not isinstance(message, str):
            message = str(message)

        response = await self._request(
            method="POST",
            headers=await self._auth_header,
            url="https://api.avito.ru/ratings/v1/answers",
            json={
                "reviewId": review_id,
                "message": message
            }
        )

        return CreateReviewAnswerV1(**response)

    async def remove_review_answer_v1(
        self,
        answer_id: int,
    ) -> bool:
        """
        https://developers.avito.ru/api-catalog/ratings/documentation#operation/removeReviewAnswerV1

        :return:
        """
        if not isinstance(answer_id, int):
            raise TypeError("answer_id must be an integer")

        response = await self._request(
            method="DELETE",
            headers=self._auth_header,
            url=f'https://api.avito.ru/ratings/v1/answers/{answer_id}',
        )

        return response.get('success', False)

    async def get_ratings_info_v1(self) -> RatingsInfoV1Response:
        """
        https://developers.avito.ru/api-catalog/ratings/documentation#operation/getRatingsInfoV1

        :return:
        """
        response = await self._request(
            method="GET",
            headers=self._auth_header,
            url="https://api.avito.ru/ratings/v1/info",
        )

        return RatingsInfoV1Response(**response)

    async def get_reviews_v1(
        self,
        limit: int = 50,
        offset: int = 0,
    ) -> ReviewsV1Response:
        """
        https://developers.avito.ru/api-catalog/ratings/documentation#operation/getReviewsV1

        :return:
        """
        if not isinstance(limit, int):
            limit = 50

        if not isinstance(offset, int):
            offset = 0

        response = await self._request(
            method="GET",
            headers=self._auth_header,
            url="https://api.avito.ru/ratings/v1/reviews",
            params={
                'limit': limit if limit > 0 else 50,
                'offset': offset if offset > 0 else 0,
            }
        )

        return ReviewsV1Response(**response)

    async def get_all_reviews_v1(self) -> typing.AsyncGenerator[ReviewsV1Response, None]:
        """
        https://developers.avito.ru/api-catalog/ratings/documentation#operation/getReviewsV1

        :return:
        """
        offset = 0

        while True:
            reviews = await self.get_reviews_v1(limit=50, offset=offset)

            yield reviews

            if not reviews.reviews or len(reviews.reviews) < 50:
                break

            offset += 50
