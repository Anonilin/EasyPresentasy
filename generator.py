from pptx import Presentation
import main # My file with main programm
from tkinter.messagebox import showinfo, showwarning

def generate(slides_list:dict, file_name='EasyPresentasy', style='default'):
    presentation = Presentation()
    for i in range(len(slides_list)):
        currentSlide = slides_list[i]
        print(currentSlide.title, currentSlide.subtitle, currentSlide.text, currentSlide.id)
        
        
        if (currentSlide.id == 0):
            if(currentSlide.title != ''):
                first_slide = presentation.slide_layouts[0]
                slide = presentation.slides.add_slide(first_slide)
                
                slide.shapes.title.text = currentSlide.title
                
            if(currentSlide.subtitle != ''):
                slide.placeholders[1].text = currentSlide.subtitle
            
            if(currentSlide.text != ''):
                text_box = slide.shapes.add_textbox(0,50,100,200)
                tf = text_box.text_frame

                par = tf.add_paragraph()
                par.text = currentSlide.text

        elif (currentSlide.id > 0):
            other_slide = presentation.slide_layouts[1]
            slide = presentation.slides.add_slide(other_slide)

            slide.shapes.title.text = currentSlide.title

            if(currentSlide.subtitle != ''):
                slide.placeholders[1].text = currentSlide.subtitle
            
            if(currentSlide.text != ''):
                text_box = slide.shapes.add_textbox(100,200,0,200)
                tf = text_box.text_frame

                par = tf.add_paragraph()
                par.text = currentSlide.text
                

    presentation.save(f'C:\\Users\\FiksikFur\\Desktop\\Projects\\Python\\EasyPresentasy\\{file_name}.pptx')

    showinfo("Succesfull", f"File was created with name:\n{file_name}.pptx\nIn directory: My Documents")

if __name__=="__main__":
    showwarning("Can't use", "You can't use module without main programm.")
    quit()