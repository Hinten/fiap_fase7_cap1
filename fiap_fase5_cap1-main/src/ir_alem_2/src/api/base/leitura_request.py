from pydantic import BaseModel

class LeituraRequest(BaseModel):
    serial: str
    temperature: float | None
    humidity: float | None
    lux: float | None
    soil_humidity: float | None


