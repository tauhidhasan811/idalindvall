import json
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
import os

load_dotenv()

class ConfigCloudinary:
    def __init__(self):
        self.CLOUDINARY_CLOUD_NAME=os.getenv("CLOUDINARY_CLOUD_NAME")
        self.CLOUDINARY_API_KEY=os.getenv("CLOUDINARY_API_KEY")
        self.CLOUDINARY_API_SECRET=os.getenv("CLOUDINARY_API_SECRET")

    def upload_data_to_cloudinary(self, file_path, public_id="budget_data.xlsx"):

        cloudinary.config(
            cloud_name=self.CLOUDINARY_CLOUD_NAME,
            api_key=self.CLOUDINARY_API_KEY,
            api_secret=self.CLOUDINARY_API_SECRET,
            secure=True
        )
        # upload json as raw file
        result = cloudinary.uploader.upload(
            file_path,
            resource_type="raw",
            folder="budget-data",
            public_id=public_id,
            overwrite=False
        )

        # print(result)
        return result["secure_url"]


