import sys
from datetime import date
from pathlib import Path

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from database import Base, get_db
from main import app
from models import Employee


test_engine = create_engine(
	"sqlite:///:memory:",
	connect_args={"check_same_thread": False},
	poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(
	autocommit=False,
	autoflush=False,
	bind=test_engine,
)


def override_get_db():
	db = TestingSessionLocal()
	try:
		yield db
	finally:
		db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
def reset_test_database():
	Base.metadata.drop_all(bind=test_engine)
	Base.metadata.create_all(bind=test_engine)

	db = TestingSessionLocal()
	db.add(
		Employee(
			id=1,
			name="Seed Employee",
			email="seed.employee@example.com",
			department="IT",
			salary=30000,
			joining_date=date(2026, 1, 1),
			is_active=True,
		)
	)
	db.commit()
	db.close()
