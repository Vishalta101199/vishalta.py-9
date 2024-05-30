from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

test_data = [
    {"username": "invalid_user", "expected_message": "Invalid credentials"},  # Negative login
    {"username": "", "expected_message": "Username cannot be empty"},  # Empty username
]

# Additional data for header and menu validation can be added here

def test_forgot_password_link(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    forgot_password_link = driver.find_element(By.LINK_TEXT, "Forgot password?")
    forgot_password_link.click()

    username_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "reset-password-username"))
    )
    assert username_box.is_displayed()

    # Simulate entering username (implement based on actual UI)
    username_box.send_keys("test_user")

    reset_button = driver.find_element(By.ID, "btn-reset-password")
    reset_button.click()

    # Validate reset password success message (adjust based on actual message)
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "authentication-message"))
    )
    assert "reset password link sent successfully" in success_message.text

def test_admin_page_header(driver):
    # Login logic (can be reused from other tests)
    # ...

    # Validate page title
    assert driver.title == "OrangeHRM"

    # Validate header options (adjust selectors based on actual UI)
    header_options = driver.find_elements(By.CSS_SELECTOR, ".head .h1")
    expected_options = ["User Management", "Job", "Organization", "Qualification"]
    assert all(option.text in expected_options for option in header_options)

def test_admin_page_menu(driver):
    # Login logic (can be reused from other tests)
    # ...

    # Validate menu options (adjust selectors based on actual UI)
    menu_items = driver.find_elements(By.CSS_SELECTOR, "#sidenav .first-level")
    expected_items = [
        "Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance",
        "Dashboard", "Directory", "Maintenance", "Buzz"
    ]
    assert all(item.text in expected_items for item in menu_items)

@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Adjust for your chosen browser
    yield driver
    driver.quit()

@pytest.mark.parametrize("data", test_data)
def test_login_negative(setup, data):
    driver = setup
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Login logic with username from data
    username_box = driver.find_element(By.ID, "username")
    username_box.send_keys(data["username"])

    password_box = driver.find_element(By.ID, "password")
    password_box.send_keys("password")  # Replace with actual password logic

    login_button = driver.find_element(By.ID, "btnSubmit")
    login_button.click()

    # Validate error message (adjust selector based on actual UI)
    error_message = WebDriverWait(driver, 10
