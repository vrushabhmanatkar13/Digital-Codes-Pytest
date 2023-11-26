from re import S
import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions


class TitleContentPageObject:
    def __init__(self, driver, baseclass):
        self.driver = driver
        self.baseclass = baseclass

    label_title_name = (By.XPATH, "//h4[@class='primary--text']")
    label_tag_name = (By.XPATH, "//div[@class='py-0 col col-auto']/span")
    label_chapter_name = (By.XPATH, "//div[@class='py-0 col']/p")
    chapter_section_number = (By.XPATH, "//section[@class='chapter']")
    chapter_name = (By.XPATH, "//h1[@class='chapter']")
    section_name = (By.XPATH, "//div[@class='section-action-wrapper v-card v-sheet theme--light my-1 pr-2 pl-2 pt-2 pb-1']//h1[@class='level1']")
    subsection_name = (By.XPATH, "//div[@class='section-action-wrapper v-card v-sheet theme--light my-1 pr-2 pl-2 pt-2 pb-1']//h1[@class='level2']")

    # Notes Bookmark Share and Print
    apps_chapter_level = (By.XPATH, "//section[@class='chapter']/div/i")
    notes = (By.XPATH, "//div[@style='display: block;']/i[text()=' border_color']")
    bookmark = (By.XPATH, "//div[@style='display: block;']/i[text()='bookmark_border']")
    share = (By.XPATH, "//div[@style='display: block;']/i[text()='link']")
    print = (By.XPATH, "//div[@style='display: block;']/i[text()='local_printshop']")

    textbox_description = (By.XPATH, "//div[@class='ql-editor ql-blank']")
    button_save = (By.XPATH, "//span[text()='Save']")
    button_new_tag = (By.XPATH, "//span[text()='New Tag']")
    textbox_tag_name = (By.XPATH, "//input[@placeholder='Tag Name']")
    button_save_tag = (By.XPATH, "//div[@style='z-index: 204;']//span[text()='Save']")
    selected_tag = (By.XPATH, "//div[@class='v-select__selections']/span")
    all_tags = (By.XPATH, "//div[@role='listbox']//div[@class='v-list-item__title']")

    button_add_more = (By.XPATH, "//button[@data-qa='share-section-modal-add-more']")
    textbox_email_0 = (By.XPATH, "//input[@data-qa='share-section-modal-email-0']")
    textbox_email_1 = (By.XPATH, "//input[@data-qa='share-section-modal-email-1']")
    button_remove = (By.XPATH, "//button[@data-qa='share-section-modal-remove-1']")
    button_share = (By.XPATH, "//button[@data-qa='share-section-modal-share']")
    button_copyurl = (By.XPATH, "//span[contains(text(),'Copy URL')]")
    button_close = (By.XPATH, "//button[@data-qa='share-section-modal-close']")
    copy_share_alert = (By.XPATH, "//div[@class='v-alert__content']")

    # Notes Bookmark Content
    selected_text = (By.XPATH, "//p[@class='note-list-quote font-italic pa-1 mb-0 mt-1 left']")
    description = (By.XPATH, "//div[@class='caption cl description']/p")
    project_tag = (By.XPATH, "(//h5[@class='font-weight-regular left'])[1]")
    created_by = (By.XPATH, "(//h5[@class='font-weight-regular left'])[2]")

    @allure.step("Get Title Name from Content")
    def get_Title_name_from_content(self):
        """
        Get Title Name form heading of content
        :return: str - title name
        """
        text = self.baseclass.gettext(self.label_title_name)
        with allure.step(text):
            return text

    @allure.step("Get Tag Name from Content")
    def get_tag_from_content(self):
        """
        Get title tag name from heading of content
        :return: str - title tag name
        """
        text = self.baseclass.gettext(self.label_tag_name)
        with allure.step(text):
            return text

    @allure.step("Get Chapter Name from Content")
    def get_chapter_name_from_content(self):
        """
        Get chapter name form heading of content
        :return: str - chapter name
        """
        text = self.baseclass.gettext(self.label_chapter_name)
        with allure.step(text):
            return text

    def get_chapter_section_number(self):
        element: WebElement = self.baseclass.find(self.chapter_section_number)
        return element.get_attribute("section-number")

    @allure.step("Double click on text")
    def doubleclick_on_chapter(self):
        """
        Double-click on Chapter heading
        :return:
        """
        action: ActionChains = self.baseclass.action_chain()
        element = self.baseclass.wait_until(self.chapter_name)
        action.double_click(element).perform()

    @allure.step("Get Chapter name")
    def get_opened_chapter_name(self):
        """
        Chapter content is displayed
        :return str: Chapter Name
        """
       # element: WebElement = self.baseclass.wait_until(self.chapter_name)
        element = self.baseclass.gettext(self.chapter_name)
        with allure.step(f"Chapter Name:{element}"):
            return element

    @allure.step("Get Section name")
    def get_opened_section_name(self):
        """
        Section content is displayed
        :return:
        """
        element = self.baseclass.gettext(self.section_name)
        with allure.step(f"Section Name: {element}"):
            return element

    @allure.step("Get Sub-Section name")
    def get_opened_subsection_name(self):
        """
        Subsection content is displayed
        :return:
        """
        element = self.baseclass.gettext(self.subsection_name)
        with allure.step(f"SubSection Name: {element}"):
            return element

    @allure.step("Click Apps icon")
    def click_apps(self):
        """
        click on waffle icon
        :return:
        """
        self.baseclass.click(self.apps_chapter_level)

    @allure.step("Click Notes")
    def click_notes(self):
        """
        click on notes waffle icon
        :return:
        """
        self.baseclass.click(self.notes)

    @allure.step("Click Bookmark")
    def click_bookmark(self):
        """
        click on bookmark waffle icon
        :return:
        """
        self.baseclass.click(self.bookmark)

    @allure.step("Enter {description}")
    def enter_Description(self, description):
        """
        Enter Description in Notes/Bookmark textbox
        :param description:
        :return:
        """
        self.baseclass.sendkeys(self.textbox_description, description)

    @allure.step("Click Save")
    def click_save(self):
        """
        click on save notes/bookmark button
        :return:
        """
        self.baseclass.click(self.button_save)

    @allure.step("Create Tag")
    def create_tag(self, tag_name):
        """
        Create New tag
        :param tag_name:
        :return:
        """
        with allure.step("Click New tag"):
            self.baseclass.click(self.button_new_tag)
        with allure.step(f"Enter {tag_name}"):
            self.baseclass.sendkeys(self.textbox_tag_name, tag_name)
        with allure.step("Click Save"):
            self.baseclass.click(self.button_save_tag)

    def wait_for_selected_tag(self):
        """
        Get selected tag name
        :return: tag_name
        """
        self.baseclass.wait.until_not(expected_conditions.text_to_be_present_in_element(self.selected_tag, "Default"))
        tag = self.baseclass.gettext(self.selected_tag)
        with allure.step(f"Selected tag_name {tag}"):
            return tag

    @allure.step("Select Tag")
    def select_tag(self, tag_name):
        """
        Select tag from list of existing tag
        :param tag_name:
        :return:
        """
        self.baseclass.click(self.selected_tag)
        tags: list[WebElement] = self.baseclass.find_elements(self.all_tags)
        name = ""
        for tag in tags:
            if tag.text == tag_name:
                name = tag.text
                tag.click()
                break
        if name == "":
            raise Exception(f"{tag_name} not present in tag list")

    @allure.step("Get Notes/Bookmark Content")
    def get_Notes_Bookmark_content(self, description_text, tag_name, created_by):
        """
        Get Notes/Bookmark Content
        ex. Description , Tag Name , Created By
        :param description_text:
        :param tag_name:
        :param created_by:
        :return:
        """
        description = self.baseclass.gettext(self.description)
        tag = self.baseclass.gettext(self.project_tag)
        created = self.baseclass.gettext(self.created_by)
        with allure.step(f"Description: {description}"):
            pass
        with allure.step(f"Tag: {tag}"):
            pass
        with allure.step(f"Created: {created}"):
            if description == description_text and tag == "Project Tag: " + tag_name and created == "Created By: " + created_by:
                return True
            else:
                raise Exception(f"Actual Description: {description},{tag},{created}")

    @allure.step("Copy Url")
    def copy_url(self):
        """
        Copy the section link url
        :return:
        """
        with allure.step("click share"):
            self.baseclass.click(self.share)
        with allure.step("click Copy Url"):
            time.sleep(1)
            self.baseclass.click(self.button_copyurl)

    @allure.step("Get Alert text")
    def get_alert_text(self):
        """
        Get Alert text after copy/share section link
        :return: Alert text
        """
        text = self.baseclass.gettext(self.copy_share_alert)
        with allure.step(f"Alert Text: {text}"):
            return text

    @allure.step("Click Close")
    def click_close(self):
        """
        click close button from alert
        :return:
        """
        self.baseclass.click(self.button_close)

    @allure.step("Share section link")
    def share_section_link(self, email):
        """
        Add more email text box and Share Section link
        :param email:
        :return: New Email textbox is displayed
        """
        with allure.step("click share"):
            self.baseclass.click(self.share)
        with allure.step("Enter email"):
            self.baseclass.sendkeys(self.textbox_email_0, email)
        with allure.step("click add more"):
            self.baseclass.click(self.button_add_more)
        result = self.baseclass.find(self.textbox_email_1).is_displayed()
        with allure.step(f"New Email textbox is Display: {result}"):
            pass
        with allure.step("Click Remove"):
            self.baseclass.click(self.button_remove)
        with allure.step("click share"):
            self.baseclass.click(self.button_share)
        return result
