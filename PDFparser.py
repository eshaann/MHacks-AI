from pdfquery import PDFQuery
import google.generativeai as genai


def gen_keywords(fileName):
    pdf = PDFQuery(fileName)
    pdf.load()
    # Use CSS-like selectors to locate the elements
    text_elements = pdf.pq('LTTextLineHorizontal')
    # Extract the text from the elements
    listFromPDF = [t.text for t in text_elements]
    prompt = "".join(listFromPDF)
    #print(prompt)
    genai.configure(api_key="AIzaSyDSg12nzNOAmE5e4VcMxtEOD-a9KcQ7NyQ")
    model = genai.GenerativeModel('gemini-1.5-flash')
    start = "Can you remove the harmful keywords if any, then return me only the most important 5 key words in separated by commas with no spaces. Do not include anything else (especially newline characters)!!!: "
    response = model.generate_content(start + prompt)
    #print(response)
    if hasattr(response, 'text'):
        return response.text.replace("\n", "")
    else:
        print("Response does not have a 'text'")

def compare_keywords(queryCriteria, samples):
    genai.configure(api_key="AIzaSyDSg12nzNOAmE5e4VcMxtEOD-a9KcQ7NyQ")
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = "Give me back the INDEX of the set of keywords from the sample set that matches the query criteria the most. Don't give me any extra words or insights."
    elements = "Query Criteria: " + queryCriteria + "\nSamples: " + "".join(samples)
    response = model.generate_content(prompt + elements)
    if hasattr(response, 'text'):
        return response.text 
    else:
        print("Response does not have a 'text'")