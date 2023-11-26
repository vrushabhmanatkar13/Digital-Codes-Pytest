import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class TOCPageObject:
    def __init__(self, driver, baseclass):
        self.driver = driver
        self.baseclass = baseclass

    label_chapter = (By.XPATH, "//div[@class='row ma-0 row--dense align-center pl-0']")
    label_section = (By.XPATH, "//div[@class='row ma-0 row--dense align-center pl-2']")
    label_sub_section = (By.XPATH, "//div[@class='row ma-0 row--dense align-center pl-4']//a")
    button_chapter_arrow = (By.XPATH, "//div[@class='row ma-0 row--dense align-center pl-0']//button")
    button_section_arrow = (By.XPATH, "//div[@class='row ma-0 row--dense align-center pl-2']//button")

    # NOTES Section
    button_Notes = (By.XPATH, "//div[contains(text(),'Notes')]")
    section_name = (By.XPATH, "//p[@class='mb-0']/a")
    dropdown_project_tag = (By.XPATH, "//div[@class='container']//div[@class='v-input__icon v-input__icon--append']")
    list_tags = (By.XPATH,
                 "//div[@class='v-menu__content theme--light menuable__content__active']//div[@class='v-list-item__title']")
    selected_tag = (By.XPATH, "//div[@class='container']//span[@class='v-chip__content']")
    clear_icon = (By.XPATH, "//div[@class='v-select__slot']//button[@aria-label='clear icon']")
    button_move_notes = (By.XPATH, "//span[contains(text(),'Move Notes')]")
    button_manage_notes = (By.XPATH, "//span[contains(text(),'Manage Notes')]")

    @allure.step("Click Chapter {chapter_name}")
    def click_chapter_name(self, chapter_name):
        """
        Click On Chapter from TOC
        :param chapter_name: str - Name of Chapter
        :raise chapter_name: NotPresent in TOC
        :return: 
        """
        name = ""
        chapters: list[WebElement] = self.baseclass.find_elements(self.label_chapter)
        for chapter in chapters:
            if chapter.text == chapter_name:
                name = chapter.text
                self.baseclass.click_by_visibility(chapter)
                break
        if name == "":
            raise Exception(f"Chapter Name: {chapter_name} is Not Present in TOC")

    @allure.step("Click Section {section_name}")
    def click_section_name(self, section_name):
        """
        Click On Section from TOC
        :param section_name: str - name of Section
        :raise Section_Name: NotPresent in TOC
        :return:
        """
        name = ""
        sections = self.baseclass.find_elements(self.label_section)
        for section in sections:
            if section.text == section_name:
                name = section.text
                self.baseclass.click_by_visibility(section)
                break
        if name == "":
            raise Exception(f"Section Name: {section_name} is Not Present in TOC")

    @allure.step("Click SubSection {subsection_name}")
    def click_subsection_name(self, subsection_name):
        """
        Click on Sub Section from TOC
        :param subsection_name: str - name of Sub Section
        :raise subsection_name: Not Present in TOC
        :return:
        """
        name = ""
        subsections = self.baseclass.find_elements(self.label_sub_section)
        for subsection in subsections:
            if subsection.text == subsection_name:
                name = subsection.text
                subsection.click()
                break
        if name == "":
            raise Exception(f"SubSection Name: {subsection_name} is Not Present in TOC")

    def get_subsection_name(self):
        subsection = self.baseclass.find_elements(self.label_sub_section)
        return subsection[0].text

    @allure.step("Click {section_name} arrow")
    def click_section_arrow(self, section_name):
        """
        Click section arrow from TOC
        :param section_name: str - Name of section
        :return:
        """
        sections: list[WebElement] = self.baseclass.find_elements(self.label_section)
        for section in sections:
            if section.text == section_name:
                arrow = section.find_element(By.TAG_NAME, "button")
                if arrow:
                    arrow.click()

    @allure.step("click NOTES tab")
    def click_NOTES(self):
        """
        click NOTES tab from TOC
        :return:
        """
        self.baseclass.click(self.button_Notes)

    @allure.step("click Manage Notes")
    def click_Manage_notes(self):
        """
        click Manage Notes button form toc
        :return:
        """
        self.baseclass.click(self.button_manage_notes)

    @allure.step("Get Chapter/Section/Subsection Name from TOC")
    def get_Chapter_Section_name(self):
        """
        Get Chapter/Section/Subsection Name from toc
        :return: chapter/section name
        """
        name = self.baseclass.gettext(self.section_name)
        with allure.step(f"Chapter/Section in TOC: {name}"):
            return name

    @allure.step("Get Tag Name from filter tag dropdown")
    def get_tag_filter_dropdown(self, tag_name):
        """
        Get Tag from Filter tag dropdown
        :param tag_name:
        :return:
        :raise Exception: tag_name tag not present in filter tag drop down
        """
        result = False
        name = ""
        with allure.step("click filter tag dropdown arrow"):
            self.baseclass.click(self.dropdown_project_tag)
        tags = self.baseclass.find_elements(self.list_tags)
        for tag in tags:
            if tag.text == tag_name:
                name = tag.text
                result = True
                break
        with allure.step(f"Tag in Drop down {name}"):
            pass
        if name == "":
            raise Exception(f"{tag_name} this tag not present in filter tag drop down")
        return result
