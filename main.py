from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDRaisedButton, MDFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from translator import translate_text
from sign_detector import run_sign_detection
from learning import sign_up, sign_in, fetch_courses  
import os
import cv2
from kivymd.uix.label import MDLabel
import webbrowser
from plyer import filechooser

# Set window size
Window.size = (300, 500)

# Kivy screen structure
screen_helper = """
ScreenManager:
    MenuScreen:
    TranslationScreen:
    SignDetectionScreen:
    LoginScreen:
    SignUpScreen:
    CourseScreen:
    VideoScreen:

<MenuScreen>:
    name: 'menu'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            text: "Welcome to the App"
            font_style: "H4"
            halign: 'center'
            
        Image:
            source: 'C:/Users/admin/OneDrive/Desktop/Project/IEEE/vedios/WhatsApp Image 2024-10-22 at 00.12.22_8da679cd.jpg'
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1
        
        MDRaisedButton:
            text: "Text Translation"
            pos_hint: {'center_x': 0.5}
            on_release: app.go_to_translation()
        MDRaisedButton:
            text: "Hand Sign Detection"
            pos_hint: {'center_x': 0.5}
            on_release: app.go_to_sign_detection()
        MDRaisedButton:
            text: "Login"
            pos_hint: {'center_x': 0.5}
            on_release: app.go_to_login()
        MDRaisedButton:
            text: "Exit"
            pos_hint: {'center_x': 0.5}
            on_release: app.stop()

<TranslationScreen>:
    name: 'translation'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)

        Image:
            source: 'C:/Users/admin/OneDrive/Desktop/Project/IEEE/vedios/WhatsApp Image 2024-10-22 at 00.12.53_f44a26d9.jpg'
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1

        MDTextField:
            id: input_text
            hint_text: "Enter text to translate"
            multiline: True
        MDTextField:
            id: target_language
            hint_text: "Enter target language ('gu' for Gujarati, 'en' for English)"
        MDRaisedButton:
            text: "Translate"
            pos_hint: {'center_x': 0.5}
            on_release: app.translate_text()
        MDFlatButton:
            text: "Back"
            pos_hint: {'center_x': 0.5}
            on_release: app.go_back_to_menu()

<SignDetectionScreen>:
    name: 'sign_detection'
    BoxLayout:
        orientation: 'vertical'
        MDLabel:
            text: "Running Hand Sign Detection. Press 'q' to exit."
            halign: 'center'
        MDRaisedButton:
            text: "Start"
            pos_hint: {'center_x': 0.5}
            on_release: app.run_sign_detection()
        MDFlatButton:
            text: "Back"
            pos_hint: {'center_x': 0.5}
            on_release: app.go_back_to_menu()

<LoginScreen>:
    name: 'login'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)

        Image:
            source: 'C:/Users/admin/OneDrive/Desktop/Project/IEEE/vedios/WhatsApp Image 2024-10-22 at 08.56.41_9f96e7ec.jpg'
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 1

        MDTextField:
            id: username
            hint_text: "Enter username"
        MDTextField:
            id: password
            hint_text: "Enter password"
            password: True
        MDRaisedButton:
            text: "Sign In"
            pos_hint: {'center_x': 0.5}
            on_release: app.sign_in()
        MDRaisedButton:
            text: "Sign Up"
            pos_hint: {'center_x': 0.5}
            on_release: app.go_to_signup()
        MDFlatButton:
            text: "Back"
            pos_hint: {'center_x': 0.5}
            on_release: app.go_back_to_menu()

<SignUpScreen>:
    name: 'signup'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)
        MDTextField:
            id: username
            hint_text: "Enter new username"
        MDTextField:
            id: password
            hint_text: "Enter new password"
            password: True
        MDRaisedButton:
            text: "Register"
            pos_hint: {'center_x': 0.5}
            on_release: app.sign_up()
        MDFlatButton:
            text: "Back"
            pos_hint: {'center_x': 0.5}
            on_release: app.go_back_to_login()

<CourseScreen>:
    name: 'course'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        spacing: dp(20)

        MDLabel:
            text: "Available Courses"
            font_style: "H5"
            halign: 'center'
        Image:
            source: 'C:/Users/admin/OneDrive/Desktop/Project/IEEE/vedios/WhatsApp Image 2024-10-22 at 08.55.42_0c696f3e.jpg'
            allow_stretch: True
            keep_ratio: False
            size_hint: 1, 0.8


        MDBoxLayout:
            id: course_buttons
            orientation: 'vertical'

        MDFlatButton:
            text: "Share on Instagram"
            pos_hint: {'center_x': 0.5}
            on_release: app.share_on_instagram()

        MDFlatButton:
            text: "Back"
            pos_hint: {'center_x': 0.5}
            on_release: app.go_back_to_menu()

<VideoScreen>:
    name: 'video'
    BoxLayout:
        orientation: 'vertical'
        padding: dp(20)
        MDLabel:
            text: "Playing Video"
            halign: 'center'
        MDRaisedButton:
            text: "Play"
            pos_hint: {'center_x': 0.5}
            on_release: app.play_course_video()
        MDFlatButton:
            text: "Back"
            pos_hint: {'center_x': 0.5}
            on_release: app.go_back_to_course()
"""

class MenuScreen(Screen):
    pass

class TranslationScreen(Screen):
    pass

class SignDetectionScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class SignUpScreen(Screen):
    pass

class CourseScreen(Screen):
    pass

class VideoScreen(Screen):
    pass

# class MyApp(MDApp):

#     def build(self):
#         return Builder.load_file("your_kv_file.kv")

#     def share_on_instagram(self):
#         # Code for sharing course outcome to Instagram
#         # This is a placeholder for now
#         print("Sharing on Instagram...")

#     def go_back_to_menu(self):
#         self.root.current = 'menu'

class LanguageApp(MDApp):
    dialog = None

    def build(self):
        self.screen_manager = Builder.load_string(screen_helper)
        return self.screen_manager  # Return the screen manager

    def on_start(self):
        self.populate_courses()  # Populate courses after the app starts

    def populate_courses(self):
        courses = fetch_courses()  # Fetch courses from the database
        course_buttons = self.screen_manager.get_screen('course').ids.course_buttons
        course_buttons.clear_widgets()  # Clear any existing buttons

        if not courses:
            no_courses_label = MDLabel(
                text="No courses available.",
                halign='center'
            )
            course_buttons.add_widget(no_courses_label)
            return

        for course_name, video_path in courses:
            course_button = MDRaisedButton(
                text=course_name,
                pos_hint={'center_x': 0.5},
                on_release=lambda x, video_path=video_path: self.play_course_video(video_path)
            )
            course_buttons.add_widget(course_button)

    def share_on_instagram(self):
        # Placeholder code for sharing on Instagram.
        # You can integrate actual API calls or sharing logic here.
        #self.show_dialog("Sharing on Instagram...")
        instagram_url = "https://instagram.com/_kartik.1510_//"  # Replace with your Instagram username
        webbrowser.open(instagram_url)
        file_path = 'C:/Users/admin/OneDrive/Desktop/Project/IEEE/vedios/WhatsApp Image 2024-10-22 at 10.03.08_1dae5ac5.jpg'
        try:
            # Use plyer's file chooser to trigger sharing intent
            filechooser.open_file(on_selection=lambda x: self.share_to_instagram(x[0]))
        except Exception as e:
            print(f"Error sharing to Instagram: {e}")

    def share_to_instagram(self, file_path):
        try:
            # Trigger Instagram share via file path
            print(f"Sharing file: {file_path}")
            webbrowser.open(file_path)
        except Exception as e:
            self.show_dialog(f"Error sharing on Instagram: {str(e)}")
        

    #Other methods...

    def show_dialog(self, message):
        if not self.dialog:
            self.dialog = MDDialog(
                text=message,
                buttons=[MDFlatButton(text="Close", on_release=self.close_dialog)]
            )
        self.dialog.text = message
        self.dialog.open()

    def close_dialog(self, _):
        if self.dialog:
            self.dialog.dismiss()


    def go_to_translation(self):
        self.screen_manager.current = 'translation'

    def go_to_sign_detection(self):
        self.screen_manager.current = 'sign_detection'

    def go_to_login(self):
        self.screen_manager.current = 'login'

    def go_to_signup(self):
        self.screen_manager.current = 'signup'

    def go_to_course(self):
        self.screen_manager.current = 'course'

    def go_to_video(self):
        self.screen_manager.current = 'video'

    def go_back_to_menu(self):
        self.screen_manager.current = 'menu'

    def go_back_to_login(self):
        self.screen_manager.current = 'login'

    def go_back_to_course(self):
        self.screen_manager.current = 'course'

    def translate_text(self):
        input_text = self.root.get_screen('translation').ids.input_text.text.strip()
        target_language = self.root.get_screen('translation').ids.target_language.text.strip()

        if input_text == "" or target_language == "":
            self.show_dialog("Please enter both the text and target language.")
        else:
            translated_text = translate_text(input_text, target_language)
            self.show_dialog(f"Translated Text:\n{translated_text}")

    def show_dialog(self, message):
        if not self.dialog:
            self.dialog = MDDialog(
                text=message,
                buttons=[MDFlatButton(text="Close", on_release=self.close_dialog)]
            )
        self.dialog.text = message
        self.dialog.open()

    def close_dialog(self, _):
        if self.dialog:
            self.dialog.dismiss()

    def run_sign_detection(self):
        print("Running Hand Sign Detection")
        run_sign_detection()

    def sign_in(self):
        username = self.root.get_screen('login').ids.username.text.strip()
        password = self.root.get_screen('login').ids.password.text.strip()
        result = sign_in(username, password)  # Call function from learning file
        self.show_dialog(result)
        if result == "Sign-in successful!":
            self.go_to_course()

    def sign_up(self):
        username = self.root.get_screen('signup').ids.username.text.strip()
        password = self.root.get_screen('signup').ids.password.text.strip()
        result = sign_up(username, password)  # Call function from learning file
        self.show_dialog(result)
        if result == "Sign-up successful!":
            self.go_back_to_login()

    def play_course_video(self, video_path):
        print(f"Playing video: {video_path}")  # Debugging line

        # Check if the file exists
        if not os.path.exists(video_path):
            self.show_dialog("Video file not found!")
            return

        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            self.show_dialog("Error: Could not open video file")
            return

        # Play the video until it ends
        while True:
            ret, frame = cap.read()
            if not ret:
                break  # Stop if the video ends

            cv2.imshow('Video Display', frame)
            cv2.waitKey(int(1000 / cap.get(cv2.CAP_PROP_FPS)))

        cap.release()
        cv2.destroyAllWindows()
        self.show_dialog("Video display finished and your scorecard is updated.")

        

    def update_progress(user_id, course_id, video_id):
        try:
            conn = mysql.connector.connect(
                host="127.0.0.1",  # Replace with your DB details
                user="root",
                password="root",
                database="user"
            )
            cursor = conn.cursor()

            # Update the video progress to True (completed)
            query = "UPDATE progress SET completed = TRUE WHERE user_id = %s AND course_id = %s AND video_id = %s"
            cursor.execute(query, (user_id, course_id, video_id))
            conn.commit()

            # Fetch the total and completed videos for the course
            cursor.execute("SELECT COUNT(*) FROM progress WHERE user_id = %s AND course_id = %s", (user_id, course_id))
            total_videos = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM progress WHERE user_id = %s AND course_id = %s AND completed = TRUE", (user_id, course_id))
            completed_videos = cursor.fetchone()[0]

            # Calculate the progress in percentage
            progress = (completed_videos / total_videos) * 100
            return progress

        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            conn.close()

if __name__ == '__main__':
    LanguageApp().run()

