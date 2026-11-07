import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_create_user():
    """Test creating a standard user with email authentication."""
    user = User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="securepassword123"
    )
    assert user.email == "test@example.com"
    assert user.check_password("securepassword123")
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser
    # Verify UUID generation
    assert user.id is not None


@pytest.mark.django_db
def test_create_superuser():
    """Test creating a superuser."""
    admin = User.objects.create_superuser(
        username="adminuser",
        email="admin@example.com",
        password="adminpassword123"
    )
    assert admin.email == "admin@example.com"
    assert admin.is_staff
    assert admin.is_superuser
