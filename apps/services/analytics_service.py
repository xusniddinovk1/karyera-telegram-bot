from posthog import Posthog


class AnalyticsService:
    def __init__(self, api_key: str) -> None:
        self.client = Posthog(
            project_api_key=api_key,
            host="https://us.i.posthog.com"
        )

    def track(self, user_id: int, event: str, properties: dict = None) -> None:
        self.client.capture(
            distinct_id=str(user_id),
            event=event,
            properties=properties or {}
        )