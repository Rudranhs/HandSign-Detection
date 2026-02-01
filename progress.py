class ProgressScreen(Screen):
    def __init__(self, **kwargs):
        super(ProgressScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Get progress data from the backend
        response = requests.get(f'http://localhost:8000/api/progress/{user_id}/')

        if response.status_code == 200:
            progress_data = response.json()
            for progress in progress_data:
                word_label = Label(text=f"Word: {progress['word']}, Learned on: {progress['date_learned']}")
                layout.add_widget(word_label)

        self.add_widget(layout)
