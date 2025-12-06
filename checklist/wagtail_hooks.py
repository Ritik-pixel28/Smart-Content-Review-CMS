from wagtail import hooks

@hooks.register("insert_editor_js")
def checklist_js():
    # simple, safe JS string — console message dikhayega
    return """
    <script>
    // Debug message for Wagtail page editor
    console.log("Checklist panel loaded successfully!");
    </script>
    """ 