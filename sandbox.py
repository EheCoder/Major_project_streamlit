import streamlit as st
from code_editor import code_editor
st.set_page_config(layout='wide')
theme_value = "default"
custom_btns = [
 {
   "name": "Copy",
   "feather": "Copy",
   "alwaysOn": True,
   "commands": ["copyAll"],
   "style": {"top": "0.46rem", "right": "0.4rem"}
 },
 {
   "name": "Shortcuts",
   "feather": "Type",
   "class": "shortcuts-button",
   "hasText": True,
   "commands": ["toggleKeyboardShortcuts"],
   "style": {"bottom": "calc(50% + 1.75rem)", "right": "0.4rem"}
 },
 {
   "name": "Save",
   "feather": "Save",
   "hasText": True,
   "commands": ["save-state", ["response","saved"]],
   "response": "saved",
   "style": {"bottom": "calc(50% - 4.25rem)", "right": "0.4rem"}
 },
 {
   "name": "Run",
   "feather": "Play",
   "primary": True,
   "hasText": True,
   "showWithIcon": True,
   "commands": ["submit"],
   "style": {"bottom": "0.44rem", "right": "0.4rem"}
 },
] #for more buttons https://code-editor-documentation.streamlit.app/Advanced_usage#custom-buttons

col1,col2=st.columns([3,5],gap="medium")

def set_theme_val():
    #write code to set theme value
    #theme_value is the variable that holds the what musrt be the theme if you can change it by adding a responsive button close to text editor
    pass

def side_bar(sidebarContent):
    for i in sidebarContent:
        st.sidebar.header(str(i))

def left_side(question,explanation,example):
    with col1:
        st.subheader(question)
        st.write(explanation)
        for i in example:
            st.write(i)
    pass

def right_side(initial_text_in_editor):
    with col2:
        response_dict = code_editor(initial_text_in_editor,
                                    height=[20, 30],
                                    theme=theme_value,
                                    shortcuts="vscode",
                                    focus=True,
                                    buttons=custom_btns)
        #print( response_dict['text'] )
        f = open("AnswerFile.txt", "w")
        f.write(response_dict['text'])
        pass


def sandbox_codeEditor(question , explanation , example_list , content_list_of_sidebar , initial_text_in_editor="#Write you code here" ):
    side_bar(content_list_of_sidebar)
    
    left_side(question , explanation , example_list)
    right_side(initial_text_in_editor)
    pass


# l1=["aaaa","bbbb","cccc"]
# side_bar(l1)
# left_side("quest1",'sbdajdsdvshdsvsfv sfbvdbf sbdajdsdvshdsvsfv sfbvdbf sbdajdsdvshdsvsfv sfbvdbf sbdajdsdvshdsvsfv sfbvdbf sbdajdsd',l1)
# print(right_side("#Write you code here test subject"))


