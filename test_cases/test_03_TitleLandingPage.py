from optparse import Option
import time

import allure
import pytest

from test_cases.test_base import TestBase
from utiilites import read_excle
from utiilites.BaseClass import BaseClass
from utiilites.Logger import get_logger


@allure.feature("Title Landing Page and TOC of Title")
class Test_TitleLandingPage(TestBase):
    subscription = ""
    info = {}

    @allure.title("Class Setup")
    def test_classSetup(self):
        user_data = read_excle.get_data_for_smoke("login", "Verify Login with valid username and password")
        self.headerpage.click_Signin()
        Test_TitleLandingPage.subscription = self.loginpage.login(user_data[0], user_data[1])
        Test_TitleLandingPage.info = self.headerpage.get_name_email()
        time.sleep(1)

    @allure.title("Test Landing Page")
    @allure.tag("Landing Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description(
        "Verify that user able to navigate to landing page of title and verify the tag and active premium text for premium title")
    @pytest.mark.parametrize(["OptionL1", "OptionL2", "OptionL3", "Title_Name", "Tag"],read_excle.get_data("Premium Complete", "Verify Title Landing Page for PC"))
    def test_Title_Landing_Page(self, request, OptionL1, OptionL2, OptionL3, Title_Name, Tag):
        """
        Test case for verify landig page, tag name and Active Premium Text for title
        """
        test_logger = get_logger(request.node.name)
        self.click_Title_Cover(OptionL1, OptionL2, OptionL3, Title_Name)
        title_name = self.titlelandingpage.get_title_name()
        tag_name = self.titlelandingpage.get_title_tag()
        trial_text = self.titlelandingpage.get_Start_Trial_text(Test_TitleLandingPage.subscription)
        premium_text = self.titlelandingpage.get_active_premium_text(tag_name)
        # category = self.titlelandingpage.get_first_category()

        """
        Assertions for Title name , Tag name and Active Premium text
        """
        BaseClass.assert_equals(Title_Name, title_name, test_logger)
        BaseClass.assert_equals(Tag, tag_name, test_logger)
        if trial_text != "":
            BaseClass.assert_equals("Start Free 14-day Premium Complete Trial", trial_text, test_logger)
        if premium_text != "":
            BaseClass.assert_equals("You have an active premium subscription to access this title", premium_text,test_logger)

    # BaseClass.assert_equals(OptionL3, category, test_logger)

    @allure.title("Test Change version of Title")
    @allure.tag("Landing Page")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify that user able to Change version of title ")
    def test_Change_Version(self, request):
        """
        Test case for Change version form to older version
        """
        test_logger = get_logger(request.node.name)
        self.click_Title_Cover("Browse Contents", "I-Codes", "2021 I-Codes", "2021 International Building Code (IBC)")
        current_version = self.titlelandingpage.verify_current_version()
        result = self.titlelandingpage.change_version()
        """
        Assertion for Current viewing text is equal to Selected text Chang version to Older version 
        """
        BaseClass.assert_True(current_version, test_logger)
        BaseClass.assert_True(result, test_logger)

    @allure.title("Test Navigate to Chapter, Section and Sub Section")
    @allure.tag("Landing Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify that user able to navigate to Chapter, Section and SubSection of title from TOC")
    def test_NavigateTo_Chapter_Section_Subsection_from_TOC(self, request):
        """
        Test Case for Verify that user able to navigate to chapter, section and subsection from TOC
        :param request:
        :return:
        """
        test_logger = get_logger(request.node.name)
        self.click_Title_Cover("Browse Contents", "I-Codes", "2021 I-Codes", "2021 International Building Code (IBC)")
        self.toc.click_chapter_name("CHAPTER 2 DEFINITIONS")
        result = self.contentpage.get_opened_chapter_name()
        """
        Assertion for Chapter content, title heading name, chapter heading name is displayed
        """
        BaseClass.assert_equals("CHAPTER 2 DEFINITIONS", result, test_logger)
        BaseClass.assert_equals("2021 International Building Code (IBC)",self.contentpage.get_Title_name_from_content(), test_logger)
        BaseClass.assert_equals("PREMIUM", self.contentpage.get_tag_from_content(), test_logger)
        BaseClass.assert_equals("CHAPTER 2 DEFINITIONS", self.contentpage.get_chapter_name_from_content(), test_logger)

        self.toc.click_section_name("SECTION 201 GENERAL")
        section = self.contentpage.get_opened_section_name()

        self.toc.click_section_arrow("SECTION 201 GENERAL")
        self.toc.click_subsection_name("201.1 Scope.")
        subsection = self.contentpage.get_opened_subsection_name()
        """
        Assertion for Section and Sub Section content is displayed
        """
        BaseClass.assert_equals("SECTION201GENERAL", section, test_logger)
        BaseClass.assert_equals("201.1Scope.", subsection, test_logger)

    @allure.title("Test Create Notes at Chapter level")
    @allure.tag("Content Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify that user able to create notes at chapter level")
    def test_Create_Notes_at_Chapter(self, request):
        """
        Test Case for Create Notes at Chapter Level
        """

        test_logger = get_logger(request.node.name)
        self.click_Title_Cover("Browse Contents", "I-Codes", "2021 I-Codes", "2021 International Building Code (IBC)")
        self.toc.click_chapter_name("CHAPTER 2 DEFINITIONS")
        self.contentpage.doubleclick_on_chapter()
        self.contentpage.click_notes()
        self.contentpage.enter_Description("Notes From Chapter Level")
        self.contentpage.create_tag("Premium")
        tag_name = self.contentpage.wait_for_selected_tag()
        self.contentpage.click_save()
        time.sleep(1)
        notes_result = self.contentpage.get_Notes_Bookmark_content("Notes From Chapter Level", tag_name, self.info.get("name") + " (" + self.info.get("email") + ")")
        """ TOC """
        self.toc.click_NOTES()
        chapter_name = self.toc.get_Chapter_Section_name()
        tag_present = self.toc.get_tag_filter_dropdown(tag_name)
        self.toc.click_Manage_notes()
        """
        Assertion for validate Title name in My notes
        """
        BaseClass.assert_equals("2021 International Building Code (IBC)", self.mynotes.get_title_name(), test_logger)

        result_mynotes = self.mynotes.get_Notes_Bookmark_Details("CHAPTER 2 DEFINITIONS", "Notes From Chapter Level",self.info.get('name'), tag_name)
        """
        Assertion for Validate Note Data form Content of Title, my notes
        """
        BaseClass.assert_True(notes_result, test_logger)

        BaseClass.assert_True(result_mynotes, test_logger)
        BaseClass.assert_True(self.mynotes.get_TimeStamp(), test_logger)
        BaseClass.assert_True(self.mynotes.get_Selected_text(), test_logger)
        self.mynotes.remove_Notes_Bookmark()
        """
        Assertion for validate Chapter/Section Name and Tag name from TOC
        """
        BaseClass.assert_equals("CHAPTER 2 DEFINITIONS", chapter_name, test_logger)
        BaseClass.assert_True(tag_present, test_logger)

    @allure.title("Test Create Bookmark at Chapter level")
    @allure.tag("Content Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify that user able to create Bookmark at chapter level")
    def test_Create_Bookmark_at_Chapter(self, request):

        test_logger = get_logger(request.node.name)
        self.click_Title_Cover("Browse Contents", "I-Codes", "2021 I-Codes", "2021 International Building Code (IBC)")
        self.toc.click_chapter_name("CHAPTER 2 DEFINITIONS")
        self.contentpage.click_apps()
        self.contentpage.click_bookmark()
        self.contentpage.enter_Description("Bookmark From Chapter Level")
        time.sleep(1)
        self.contentpage.select_tag("Premium")
        tag_name = self.contentpage.wait_for_selected_tag()
        self.contentpage.click_save()
        time.sleep(1)
        notes_result = self.contentpage.get_Notes_Bookmark_content("Bookmark From Chapter Level", tag_name,self.info.get("name") + " (" + self.info.get("email") + ")")
        """ TOC """
        self.toc.click_NOTES()
        chapter_name = self.toc.get_Chapter_Section_name()
        tag_present = self.toc.get_tag_filter_dropdown(tag_name)
        self.toc.click_Manage_notes()
        """
        Assertion for validate Title name in My notes
        """
        BaseClass.assert_equals("2021 International Building Code (IBC)", self.mynotes.get_title_name(), test_logger)

        result_mynotes = self.mynotes.get_Notes_Bookmark_Details("CHAPTER 2 DEFINITIONS", "Bookmark From Chapter Level", self.info.get('name'), tag_name)
        """
        Assertion for Validate Note Data form Content of Title, my notes
        """
        BaseClass.assert_True(notes_result, test_logger)

        BaseClass.assert_True(result_mynotes, test_logger)
        BaseClass.assert_True(self.mynotes.get_TimeStamp(), test_logger)
        self.mynotes.remove_Notes_Bookmark()
        """
        Assertion for validate Chapter/Section Name and Tag name from TOC
        """
        BaseClass.assert_equals("CHAPTER 2 DEFINITIONS", chapter_name, test_logger)
        BaseClass.assert_True(tag_present, test_logger)

    @allure.title("Test Copy and Share link Chapter level")
    @allure.tag("Content Page")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify that user able to Copy and Share section link chapter level")
    def test_Copy_Share_link_at_Chapter(self, request):
        """
        Test case for Copy section link and share section url from content of title
        """
        test_logger = get_logger(request.node.name)
        self.click_Title_Cover("Browse Contents", "I-Codes", "2021 I-Codes", "2021 International Building Code (IBC)")
        self.toc.click_chapter_name("CHAPTER 2 DEFINITIONS")
        self.contentpage.click_apps()
        self.contentpage.copy_url()
        copy_url = self.contentpage.get_alert_text()
        self.contentpage.click_close()

        result = self.contentpage.share_section_link("test.user@iccsafe.info")
        share_link = self.contentpage.get_alert_text()
        """
        Assertion for get Alert text for Copy and Share section url
        """
        BaseClass.assert_equals("Link copied to clipboard.", copy_url, test_logger)
        BaseClass.assert_equals("Section link shared successfully!", share_link, test_logger)
        BaseClass.assert_True(result, test_logger)
