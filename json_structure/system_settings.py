class SystemSettings:
    off_topic = {
        "enabled": True
    }
    disambiguation = {
                         "prompt": "Did you mean:",
                         "enabled": True,
                         "randomize": True,
                         "max_suggestions": 5,
                         "suggestion_text_policy": "title",
                         "none_of_the_above_prompt": "None of the above"
                     },
    intent_classification = {
                                "training_backend_version": "v2"
                            },
    spelling_auto_correct = True
