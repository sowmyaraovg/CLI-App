import json

from colorama import init, Fore,Style,Back
init(convert=True)
init(autoreset=True)
def deploymentscenarios():
    # Read a json file
    with open('SampleData.json') as json_data:
        d1 = json.load(json_data)
    #d2 contains list of 'Content;
        d2=d1["Content"][1]
        #List of sectiontitle and scenario 
        sectionlist=[]
        scenariolist=[]
        docnamelist=[]
        
        #Append the section list 
        for sl in d1['Content']:
            sectionlist.append(sl['SectionTitle'])
        
        print(Fore.GREEN +"SECTION TITLES WITH THEIR INDEX")

        # To print the section with index    
        for i, element in enumerate(sectionlist):    
            print(Fore.RED + "{0} with index   :{1}".format(element,i)) 
        
            
        answer=input(Fore.GREEN + "Enter the index of the SectionTitle or type 'N' to enter new section    :")
        # New Section enter here
        if (answer=='N'):
            #New section and Scenario")
            SectionTitle=input("Enter the Section Title:")     
            sectionlist.append(SectionTitle)
            SceanrioName=input("Enter ScenarioName")
            scenariolist.append(ScenarioName)
            Description=input("Enter Description")
            response=None
            for response in {"Docs","Gaps","exit"}:
                response = input("Please enter 1 for Docs' 2 for Gaps and 0 for exit: ")
                if (response =='1'):
                    Name=input("enter the name of the docs   :")
                    Link=input("enter the Url of the Docs    :")
                        
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
        #Sections already present enter this loop
        else:    
            sect_ind=int(answer)
            Section_Title=sectionlist[sect_ind]
            print(Fore.RED +"You are in the {0} in this section".format(Section_Title))
            #Append the scenario list 
            for sc in d1['Content'][sect_ind]['SectionContent']:
                scenariolist.append(sc['ScenarioName'])

            print(Fore.GREEN + "SCENARIO NAMES WITH THEIR INDEX")    

            # To print the scenarios with index    
            for i, element in enumerate(scenariolist):
                print(Fore.RED + "{0} with index {1}".format(element,i))
            
            resp=input("Enter the index of the scenario to access or type 'N' to enter new scenario   :")
            #New Scenarios enter this loop
            if (resp=='N'):
                #enter new scenario,description
                ScenarioName=input("Enter ScenarioName")
                scenariolist.append(ScenarioName)
                Description=input("Enter Description")
                response=None
                for response in {"Docs","Gaps","exit"}:
                    response = input("Please enter 1 for Docs' 2 for Gaps and 0 for exit: ")
                    if (response =='1'):
                        Name=input("enter the name of the docs   :")
                        Link=input("enter the Url of the Docs    :")
                        docnamelist.append(Name)   
                        
            
                    
                    elif (response =='2'):
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

                    elif(response=='0'):
                        break       
            #Scenarios already present enter this loop   
            else:
                scenario_ind=int(resp)
                scenario_name= scenariolist[scenario_ind]
                print(Fore.RED +"You are in the {0} in this scenario".format(scenario_name))
                
                #append all 'Name' in List
                for docname in d1['Content'][sect_ind]['SectionContent'][1]['Docs']:
                    docnamelist.append(docname['Name'])

                response=None
                for response in {"Docs","Gaps","exit"}:
                    response = input("Please enter 1 for Docs' 2 for Gaps and 0 for exit: ")
                    if (response =='1'):
                        Name=input("enter the name of the docs   :")
                        #Check if note exists
                        if Name not in docnamelist:
                            Link=input("enter the Url of the Docs    :")
                            docnamelist.append([Name])
        
                        else:
                            print("Note Already exists")
            
                    
                    elif (response =='2'):
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

                    elif(response=='0'):
                        break       

    d1 = {"Content":[{"SectionTitle":Section_Title,"SectionContent":[{"ScenarioName":scenario_name,"Description":"Description","Docs":{"Name":Name,"Link":Link},"Gaps":[{"Url":"#","Description":Desc,"CreationDate":CreationDate,"VSTSLink":Vstslink,"Tags":Tags,"Categories":Categories,"Sources":[Hackevent,Name,TeamName]}]}]}]}

    # with open('data12.json', 'a') as outfile:  
    #     json.dump(d1, outfile,indent=2) 
    
    a = []
    if not os.path.isfile('data12.json'):
        a.append(d1)
        with open('data12.json', mode='w') as f:
            f.write(json.dumps(d1, indent=2))
    else:
        with open('data12.json') as feedsjson:
            feeds = json.load(feedsjson)

        feeds.append(d1)
        with open('data12.json', mode='w') as f:
            f.write(json.dumps(feeds, indent=2))


    output=json.dumps(d1,indent=2)   
    print(output)
if __name__ == '__main__':
    print('call deploymentscenarios()')
    deploymentscenarios()    
  
           