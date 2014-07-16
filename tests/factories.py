from factory.alchemy import SQLAlchemyModelFactory

from publictitles.models import Title
from publictitles import db

class TitleFactory(SQLAlchemyModelFactory):

    class Meta:
        model = Title
        sqlalchemy_session = db.session

    title_number = "TN1234567"
    address  = "1 High Street"
    postcode = "ABC 123"
