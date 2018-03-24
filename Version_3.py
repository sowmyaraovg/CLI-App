import json
from collections import defaultdict
from colorama import init, Fore,Style,Back


# This function returns a list of section    
def sectiontitle_list():
    """ When a user enters the application a list of section present are displayed  """
    sec_list=[]
    sec_list=[d['SectionTitle'] for d in content_dict['Content']]
    return sec_list

# This returns list of scenarios based on the section index enumerated thru section name selection
def scenario_list(section_index):
    """When a user selects a section from the section list, the scenarios present in that particular section are displayed """
    scenario_list=[]
    for sc in content_dict['Content'][section_index]['SectionContent']:
        scenario_list.append(sc['ScenarioName'])
    return scenario_list

#This list returns the Name of Docs in each section.  
def get_doc_name(section_index,scenario_index):
    """When a user selects a scenario from the scenario list,the list of Name of docs are displayed"""
    doc_list=[]
    for docname in content_dict['Content'][section_index]['SectionContent'][scenario_index]['Docs']:
        doc_list.append(docname['Name'])
    return doc_list

#This list returns Gaps list in each section 
def Get_Gaps(section_index,scenario_index):
    """When a user selects a scenario from the scenario list,the list of gaps description are displayed"""
    gap_list=[]
    for gap in content_dict['Content'][section_index]['SectionContent'][scenario_index]['Gaps']:
        gap_list.append(gap['Description'])
    return gap_list

#This list enumerates and prints items with their index
def print_lists(list1):
    """ This function enumerates lists and prints the item and their index in the list"""
    for i, element in enumerate(list1):
        print (Fore.RED + "{0} with index   :{1}".format(element,i)) 


#This function is used when section and scenrio is known and we add docs(appending)
def add_docs(content_dict1,section_index,scenario_index,Name,Link):
    """ To add new docs to the section"""
    docs_dict={}
    docs_dict={"Name":Name,"Link":Link}
    content_dict1['Content'][section_index]['SectionContent'][scenario_index]['Docs'].append(dict(docs_dict))
    return content_dict1  

#This function is used when section and scenrio is known and we add gaps(appending)   
def add_gaps(content_dict1,section_index,scenario_index,Desc,url,cdate,vsts,tags,cat,*sources):
    """To add new Gaps to the section"""
    gaps_dict={}
    gaps_dict={"Description":Desc,"Url":url,"CreationDate":cdate,"VSTSLink":vsts,"Tags":tags,"Categories":cat,"Sources":sources}
    content_dict1['Content'][section_index]['SectionContent'][scenario_index]['Gaps'].append(dict(gaps_dict))
    return content_dict1

#this function is used when we have a known section,we insert a scenario,docs/gaps
def add_scenario(content_dict1,section_index,ScenarioName,Description):
    """To add a new sceanrio"""
    sect_dict={"ScenarioName":ScenarioName,"Description":Description}
    response=input("Press 1 for Docs and 2 for Gaps")  
    if response=='1':
        
        Name=input("Enter the Name of the Docs  :")
        Link=input('Enter the Link of the Docs  :')
        docs_dict={"Name":Name,"Link":Link}
        doc_dict={"Docs":[docs_dict]}
        sect_dict.update(doc_dict)
        content_dict1['Content'][section_index]['SectionContent'].append(sect_dict)
        
            
    if response=='2':
       
        Desc=input("enter the description of gaps  :")
        Url=input("enter the Url of the Gaps       :")   
        CreationDate=input("enter the date created :")
        Vstslink=input("enter Vstslink             :")
        Tags=input("enter Tags                     :")
        Categories=input("enter Categories              :")
        Hackevent=input("enter the hackevent details    :")
        Name=input("enter the name                   :")
        TeamName=input("enter the team name                :")
        gaps_dict={"Description":Desc,"Url":"#","CreationDate":CreationDate,"VSTSLink":Vstslink,"Tags":Tags,"Categories":Categories,"Sources":[Hackevent,Name,TeamName]}
        gap_dict={"Gaps":[gaps_dict]}
        sect_dict.update(gap_dict)
        content_dict1['Content'][section_index]['SectionContent'].append(sect_dict)
    
    return content_dict1

    #this function inserts a new section, scenario, description,Docs or Gaps
def add_section(content_dict1,section_index,SectionTitle):
    """To add a new section"""
    scenario_index=0
    section_ind=len(sectiontitle_list())
    section_index=section_ind-1
    ScenarioName=input("Enter Scenario Name  :")
    Description=input("Enter Description  :")
    response=input("Press 1 for Docs and 2 for Gaps")  
    if response=='1':
        Name=input("Enter the Name of the Docs  :")
        Link=input('Enter the Link of the Docs  :')
        SectionContent =[{"ScenarioName":ScenarioName,"Description":Description,"Docs":{"Name":Name,"Link":Link}}]
            
    if response=='2':
        Desc=input("enter the description of gaps  :")
        Url=input("enter the Url of the Gaps       :")   
        CreationDate=input("enter the date created :")
        Vstslink=input("enter Vstslink             :")
        Tags=input("enter Tags                     :")
        Categories=input("enter Categories              :")
        Hackevent=input("enter the hackevent details    :")
        Name=input("enter the name                   :")
        TeamName=input("enter the team name                :")
        SectionContent=[{"ScenarioName":ScenarioName,"Description":Description,"Gaps":{"Description":Desc,"Url":"#","CreationDate":CreationDate,"VSTSLink":Vstslink,"Tags":Tags,"Categories":Categories,"Sources":[Hackevent,Name,TeamName]}}]
       

    sect_dict={"SectionTitle":SectionTitle,"SectionContent":SectionContent}
    content_dict1['Content'].append(dict(sect_dict))    
    return content_dict1   

#Main function which interacts with the user      
def main_function ():
    """Main function which executes the command line application"""
    
    print("WELCOME!!!")
    print('----------')
    print('          ')
    
    print(Fore.GREEN +"SECTION TITLES WITH THEIR INDEX")
    print('----------------------------------------------------------') 
    seclist=sectiontitle_list()
    # Printing the Section Title with their Index
    print_lists(seclist)
    section_index=input("Enter the index of the SectionTitle or type 'N' to enter new section    :")
    # The user enter this loop if they choose an index 
    if (section_index !='N'):
        Section_Name=seclist.__getitem__(int(section_index))
        print(Fore.GREEN+"You are in this Section -{0}" .format(Section_Name))
        print(Fore.GREEN +"SCENARIO NAMES WITH THEIR INDEX")
        print('----------------------------------------------------------') 
        sclist=scenario_list(int(section_index))
        # Printing the ScenarioName with their Index in the chosen Section
        print_lists(sclist)
        
        scenario_index=input("Enter the index of the scenario to access or type 'N' to enter new scenario   :") 
        # The user enters this loop if they choose an existing index
        if scenario_index !='N':
            newlength=int(scenario_index)
            
            Scenario_Name=sclist.__getitem__(newlength-1)
            print(Fore.GREEN+"You are in this Scenario -{0}" .format(Scenario_Name))
            response =  input("Please enter 1 for Docs' 2 for Gaps ")
            if(response=='1'):
                Name=input("Enter the Name of the Docs  :")
                Link=input('Enter the Link of the Docs  :')
                add_docs(content_dict,int(section_index),newlength-1,Name,Link)
                
            if(response=='2'):
                Desc=input("enter the description of gaps  :")
                Url=input("enter the Url of the Gaps       :")   
                CreationDate=input("enter the date created :")
                Vstslink=input("enter Vstslink             :")
                Tags=input("enter Tags                     :")
                Categories=input("enter Categories              :")
                Hackevent=input("enter the hackevent details    :")
                Name=input("enter the name                   :")
                TeamName=input("enter the team name                :")
                sources=[Hackevent,Name,TeamName]
                add_gaps(content_dict,int(section_index),newlength,Desc,Url,CreationDate,Vstslink,Tags,Categories,sources)
        
        
        # The user enters this loop when new Scenario is chosen
        else:
            ScenarioName=input("Enter Scenario Name   :")
            Description=input("Enter Description   :")
            add_scenario(content_dict,int(section_index),ScenarioName,Description)
    
     # The user enters this loop when new Section is chosen
    else:
        newsection=len(sectiontitle_list())
        SectionTitle=input("Enter the Section Title  :")
        add_section(content_dict,newsection,SectionTitle)

    output2=json.dumps(content_dict,indent=2)
    print(output2)
    with open('data5.json','a+') as outfile:
       json.dump(content_dict, outfile,indent=2)        

if __name__ == '__main__':
    init(convert=True)
    init(autoreset=True)
    with open('SampleData.json') as json_data:
        content_dict= json.load(json_data)
        
    main_function()
   