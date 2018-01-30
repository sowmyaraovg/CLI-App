import json
# Read a json file
with open('SampleData.json') as json_data:
    d1 = json.load(json_data)
   #d2 contains list of 'Content;
    d2=d1["Content"][1]
    #List of sectiontitle and scenario 
    sectionlist=[]
    scenariolist=[]

    SectionTitle= "Ingest Data into Azure SQL DW Work Tables"  #input("Enter the section name:")
    ScenarioName="Provision SQL DW database"
    Description="About Azure SQL"
     #To explicitly display to the user about the Sections and Scenarios present 
    for sl in d1['Content']:
        sectionlist.append(sl['SectionTitle'])
    
    for i in range(len(sectionlist)):
        for sc in d1['Content'][i]['SectionContent']:
            scenariolist.append(sc['ScenarioName'])
            
    print("ScenarioName[]=",list(scenariolist))   
    print("SectionList[]=",list(sectionlist))
    
    # Check if sectiontitle is present and ScenarioName exists
    for sctitle in sectionlist:
        for scname in scenariolist:
            if sctitle==SectionTitle and scname ==ScenarioName:
                print("Scenario and Section exists", SectionTitle, ScenarioName)  
                # check for Dopcs,gaps,Exit           
                response=None
                for response in {"Docs","Gaps","exit"}:
                    response = input("Please enter 1 for Docs' 2 for Gaps and 0 for exit: ")
                    if (response =='1'):
                        Note1=input("enter the name of the docs   :")
                    #Check if note exists
                    #if exists then print("Note already exists")
                    #else append the new note and url
                        Link1=input("enter the Url of the Docs    :")
    
    #           else:
    #               print("Already exists")
        
                
                    if (response =='2'):
                   #?check if
                        Desc=input("enter the description of gaps  :")
                        Url=input("enter the Url of the Gaps       :")   
                        CreationDate=input("enter the date created :")
                        Vstslink=input("enter Vstslink             :")
                        Tags=input("enter Tags                     :")
                        Categories=input("enter Categories              :")
                        Hackevent=input("enter the hackevent details    :")
                        Name=input("enter the name                   :")
                        TeamName=input("enter the team name                :")

                    if(response=='0'):
                        break       
    #         else:
    #             ScenarioName=input("Enter ScenarioName :")  
    #             Description=input("Enter Description  :")  
    #             response=None
    #             for response in {"Docs","Gaps","exit"}:
    #                 response = input("Please enter 1 for Docs' 2 for Gaps and 0 for exit: ")
    #                 if (response =='1'):
    #                     Note1=input("enter the name of the docs   :")
    #                 #Check if note exists
    #                 #if exists then print("Note already exists")
    #                 #else append the new note and url
    #                     Link1=input("enter the Url of the Docs    :")
    
    # #           else:
    # #               print("Already exists")
        
                
    #                 if (response =='2'):
    #                #?check if
    #                     Desc=input("enter the description of gaps  :")
    #                     Url=input("enter the Url of the Gaps       :")   
    #                     CreationDate=input("enter the date created :")
    #                     Vstslink=input("enter Vstslink             :")
    #                     Tags=input("enter Tags                     :")
    #                     Categories=input("enter Categories              :")
    #                     Hackevent=input("enter the hackevent details    :")
    #                     Name=input("enter the name                   :")
    #                     TeamName=input("enter the team name                :")

    #             if(response=='0'):
    #                 break       



d1 = {"Content":[{"SectionTitle":SectionTitle,"SectionContent":[{"ScenarioName":ScenarioName,"Description":Description,"Docs":{Note1:Link1},"Gaps":[{"Url":"#","Description":Desc,"CreationDate":CreationDate,"VSTSLink":Vstslink,"Tags":Tags,"Categories":Categories,"Sources":[Hackevent,Name,TeamName]}]}]}]}

#with open('data9.json', 'a') as outfile:  

output=json.dumps(d1,indent=2)   
print(output)

  
           