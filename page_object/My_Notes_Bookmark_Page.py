import allure
from selenium.webdriver.common.by import By


class My_Notes_Bookmark_Page:
    def __init__(self, driver, baseclass):
        self.driver = driver
        self.baseclass = baseclass

    title_name = (By.XPATH, "//div[@class='title-card-hover']//a[@class='accent--text']")
    chapter_name = (By.XPATH, "//div[@class='v-card__title']/a")
    selected_text = (By.XPATH, "//p[@class='note-list-quote font-italic pa-1 mb-0 mt-1']")
    description = (By.XPATH, "//p[@class='mt-2 ml-1']")
    created_by = (By.XPATH, "//div[@class='d-flex']//h5[1]")
    project_tag = (By.XPATH, "//div[@class='d-flex']//h5[2]")
    timestamp = (By.XPATH, "//div[@class='d-flex']//h5[3]")
    remove_button = (By.XPATH, "//span[contains(text(),'Remove')]")
    remove_alert = (By.XPATH, "//span[text()='Remove']")

    def get_title_name(self):
        title = self.baseclass.gettext(self.title_name)
        with allure.step(f"Title name in My notes: {title}"):
            return title

    def get_Selected_text(self):
        result = self.baseclass.find(self.selected_text).is_displayed()
        with allure.step(f"Selected Text is Displayed: {result}"):
            return self.baseclass.find(self.selected_text).is_displayed()

    def get_Notes_Bookmark_Details(self, chapter_text, description_text, created_by_text, project_tag_text):
        self.baseclass.click(self.title_name)
        chapter = self.baseclass.gettext(self.chapter_name)
        description = self.baseclass.gettext(self.description)
        created_by = self.baseclass.gettext(self.created_by).replace("Created By: ", "")
        project_tag = self.baseclass.gettext(self.project_tag).replace("Project Tag: ", "")
        with allure.step(f"Chapter Name in My notes: {chapter}"):
            pass
        with allure.step(f"Description in My notes: {description}"):
            pass
        with allure.step(f"Created By in My notes: {created_by}"):
            pass
        with allure.step(f"Project Tag in My notes: {project_tag}"):
            if chapter == chapter_text and description_text == description and created_by_text == created_by and project_tag == project_tag_text:
                return True
            else:
                raise Exception(f"Actual Details :{chapter}, {description} , {created_by} , {project_tag}")

    def get_TimeStamp(self):
        result = self.baseclass.find(self.timestamp).is_displayed()
        with allure.step(f"Time Stamp is Displayed: {result}"):
            return self.baseclass.find(self.timestamp).is_displayed()

    @allure.step("Click Remove")
    def remove_Notes_Bookmark(self):
        self.baseclass.click(self.remove_button)
        self.baseclass.click(self.remove_alert)
