from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime

# User Information Entry:
links = ["https://www.tesla.com/careers/search/job/apply/232397","https://www.tesla.com/careers/search/job/apply/232150"]
#link = "https://www.tesla.com/careers/search/job/apply/234095"
first_name = "Andrew"
last_name = "Phung"
phone_number = "6264563506"
phone_type = "mobile"
email = "andrewphung@berkeley.edu"
country = "US"
gender = "male"
today_date = "December 2024"
graduation_year = "2025"
graduation_date = "December 2025"
profile_link = "https://www.linkedin.com/in/andrewphung1/"
resume = r"C:\Users\msf\Downloads\Andrew_Phung_Resume_2026.pdf"

# Set Up Time

def get_next_month(current_month):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    current_month_name, current_year = current_month.split()
    current_year = int(current_year)  # Convert year to integer

    current_month_index = months.index(current_month_name)
    next_month_index = (current_month_index + 1) % 12

    if next_month_index == 0:  # If it's December, increment the year
        current_year += 1
    
    next_month_name = months[next_month_index]
    return f"{next_month_name} {current_year}"

# Set up the browser
def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")  # Open the browser maximized
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Automate the entry process
def automate_entry(link):
    driver = setup_browser()
    print("Setting Up Browser...")
    try:
        driver.get(link)
        
        # Wait for the page to load (modify selectors as necessary)
        wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds for elements
        time.sleep(2)

        # JOB APPLICATION PAGE - Step 1 of 4 
        
        print("Filling out First Page of Application...")

        first_name_button = wait.until(EC.visibility_of_element_located((By.NAME, "personal.firstName")))
        first_name_button.send_keys(first_name)
        time.sleep(0.2)

        last_name_button = driver.find_element(By.NAME, "personal.lastName")
        last_name_button.send_keys(last_name)
        time.sleep(0.2)

        phone_number_button = driver.find_element(By.NAME, "personal.phone")
        phone_number_button.send_keys(phone_number)
        time.sleep(0.2)

        phone_type_dropdown = Select(driver.find_element(By.NAME, "personal.phoneType"))
        phone_type_dropdown.select_by_value(phone_type)
        time.sleep(0.2)

        email_button = driver.find_element(By.NAME, "personal.email")
        email_button.send_keys(email)
        time.sleep(0.2)
        country_dropdown_button = Select(driver.find_element(By.NAME, "personal.country"))
        country_dropdown_button.select_by_value(country)
        time.sleep(0.2)
        
        add_profile_link_button = driver.find_element(By.CLASS_NAME, "style_AddLabel__ygIAt")
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", add_profile_link_button)
        time.sleep(0.5)
        add_profile_link_button.click()
        profile_link_submission = driver.find_element(By.NAME, "personal.profileLinks[0].link")
        profile_link_submission.send_keys(profile_link)
        time.sleep(0.2)
        
        resume_submission = driver.find_element(By.NAME, "personal.resume")
        resume_submission.send_keys(resume)
        time.sleep(0.2)

        next_page_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='tds-btn' and @name='next' and @data-action-type='next']")))
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", next_page_button)
        time.sleep(1)
        next_page_button.click()
        time.sleep(0.5)

        print("Finished First Page...Going onto the Next Page.")

        # JOB APPLICATION PAGE - Step 2 of 4

        print("Filling out Second Page of Application...")

        calendar_button = driver.find_element(By.CLASS_NAME, "tds-icon-btn")
        calendar_button.click()
        time.sleep(0.2)
        calendar_time_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".tds-day.tds-day--today")))
        time.sleep(0.2)
        calendar_time_button.click()
        time.sleep(0.2)

        months_availability_dropdown = Select(driver.find_element(By.NAME, "job.jobInternshipDuration"))
        months_availability_dropdown.select_by_value("7_months_or_more")
        time.sleep(0.2)

        part_or_fulltime_dropdown = Select(driver.find_element(By.NAME, "job.jobInternshipType"))
        time.sleep(0.2)
        part_or_fulltime_dropdown.select_by_value("full_time")
        time.sleep(0.2)

        thesis_button = driver.find_element(By.XPATH, "//input[@name='job.jobInternshipThesis' and @value='no']")
        thesis_button.click()
        time.sleep(0.2)

        next_page_button2 = driver.find_element(By.NAME, "next")
        next_page_button2.click()
        time.sleep(1)

        print("Finished Second Page...Going onto the Next Page.")

        # JOB APPLICATION PAGE - Step 3 of 4

        print("Filling out Third Page of Application...Almost There!")

        availability_or_notice_period_dropdown = Select(driver.find_element(By.NAME, "legal.legalNoticePeriod"))
        availability_or_notice_period_dropdown.select_by_value("immediately")
        time.sleep(0.2)
        
        other_considerations_button = driver.find_element(By.XPATH, "//input[@name='legal.legalConsiderOtherPositions' and @value='yes']")
        other_considerations_button.click()
        time.sleep(0.2)

        future_immigration_sponsorship_button = driver.find_element(By.XPATH, "//input[@name='legal.legalImmigrationSponsorship' and @value='no']")
        future_immigration_sponsorship_button.click()
        time.sleep(0.2)

        previous_employed_by_tesla_button = driver.find_element(By.XPATH, "//input[@name='legal.legalFormerTeslaEmployee' and @value='yes']")
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", previous_employed_by_tesla_button)
        time.sleep(0.2)
        previous_employed_by_tesla_button.click()
        time.sleep(0.2)

        former_or_current_intern_button = driver.find_element(By.XPATH, "//input[@name='legal.legalFormerTeslaInternOrContractor' and @value='yes']")
        former_or_current_intern_button.click()
        time.sleep(0.2)

        current_uni_student_button = driver.find_element(By.XPATH, "//input[@name='legal.legalUniversityStudent' and @value='yes']")
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", current_uni_student_button)
        time.sleep(0.2)
        current_uni_student_button.click()
        time.sleep(0.5)

        anticipated_graduation_date_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "tds-icon-btn")))
        anticipated_graduation_date_box.click()
        time.sleep(0.5)

        current_month_label = driver.find_element(By.XPATH, "//label[@aria-live='polite']")
        current_month = current_month_label.text
        
        print(f"Starting with current month: {current_month}")
        while True:
            print(f"Checking month: {current_month}")
            if current_month == graduation_date:
                break
            try:
                next_month = get_next_month(current_month)  
                next_month_button = driver.find_element(By.XPATH, f"//button[@aria-label='{next_month}' and @tabindex='-1']")  
                print(f"Clicking next month: {next_month}")
                next_month_button.click()
            except Exception as e:
                print(f"Error clicking the next month button: {e}")
                break
            current_month_label = driver.find_element(By.XPATH, "//label[@aria-live='polite']")
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable(current_month_label)) 
            current_month = current_month_label.text
            print(f"Current month: {current_month}")
            next_month = get_next_month(current_month)

        anticipated_graduation_day = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='tds-day' and span[text()='15']]")))
        anticipated_graduation_day.click()

        consent_for_text_messages_button = driver.find_element(By.XPATH, "//input[@name='legal.legalReceiveNotifications' and @value='yes']")
        time.sleep(0.2)
        consent_for_text_messages_button.click()
        time.sleep(0.2)

        consent_form_button = driver.find_element(By.NAME, "legal.legalAcknowledgment")
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", consent_form_button)
        time.sleep(0.2)
        consent_form_button.click()
        time.sleep(0.2)

        legal_name_fill = driver.find_element(By.NAME, "legal.legalAcknowledgmentName")
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", legal_name_fill)
        time.sleep(0.2)
        legal_name_fill.send_keys(first_name + ' ' + last_name)
        time.sleep(0.5)

        next_page_button3 = driver.find_element(By.NAME, "next")
        time.sleep(1)
        next_page_button3.click()
        time.sleep(0.5)

        print("Finished Third Page...Going onto the Final Page.")

        # JOB APPLICATION PAGE - Step 4 of 4

        print("Filling out Final Page of Application...")

        disclosure_agreement = driver.find_element(By.CLASS_NAME, "style_Disclaimer__toBo-")
        total_div_height = driver.execute_script("return arguments[0].scrollHeight", disclosure_agreement)

        while True:
            current_scroll_position = driver.execute_script("return arguments[0].scrollTop", disclosure_agreement)
            driver.execute_script("arguments[0].scrollTop += 350;", disclosure_agreement)
            time.sleep(0.2)  # Allow time for the scroll to take effect
            new_scroll_position = driver.execute_script("return arguments[0].scrollTop", disclosure_agreement)

        # Break the loop if the scroll position doesn't change or reaches the bottom
            if new_scroll_position == current_scroll_position or new_scroll_position + disclosure_agreement.size['height'] >= total_div_height:
                break

        time.sleep(0.5)


        disclosure_agreement_checkbox = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "tds-form-input")))
        time.sleep(0.2)
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", disclosure_agreement_checkbox)
        time.sleep(0.2)
        disclosure_agreement_checkbox.click()

        gender_button = Select(driver.find_element(By.NAME, "eeo.eeoGender"))
        gender_button.select_by_value(gender)
        time.sleep(0.2)

        veteran_status_button = Select(driver.find_element(By.NAME, "eeo.eeoVeteranStatus"))
        veteran_status_button.select_by_value("no")
        time.sleep(0.2)

        race_ethnicity_button = Select(driver.find_element(By.NAME, "eeo.eeoRaceEthnicity"))
        race_ethnicity_button.select_by_value("asian")
        time.sleep(0.2)

        disability_button = Select(driver.find_element(By.NAME, "eeo.eeoDisabilityStatus"))
        disability_button.select_by_value("no")
        time.sleep(0.2)

        legal_name_fill2 = driver.find_element(By.NAME, "eeo.eeoDisabilityStatusName")
        driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", legal_name_fill2)
        time.sleep(0.5)
        legal_name_fill2.send_keys(first_name + ' ' + last_name)

        submit_button = driver.find_element(By.XPATH, "//button[@class='tds-btn' and @type='submit']")
        time.sleep(0.2)
        submit_button.click()

    except WebDriverException as e:
        time.sleep(3)
        print(f"WebDriverException occurred: {e}")
        print("Interruption Happened. User May Have Closed Tab. Quitting...")
        driver.quit()
    except Exception as e:
        print("An error occured:", e) 
        driver.quit() 
    finally:
        # Keep the browser open for review
        time.sleep(3)  # Keep open for 200 seconds
        print(f"Application Submitted! Link: {link}")
        driver.close()

# automate_entry(link)
for i in range(len(links)):
    automate_entry(links[i])



