import json

class DocsClass:

  '''This is Docs class with Name, Link as Parameters'''
  def __init__(self, Name, Link):
    self.Name = Name
    self.Link = Link

class GapsClass:
  '''This is Gaps class with Description,Url,CreationDate, VSTSLink,Tags, Categories as Parameters'''
  def __init__(self, Description, Url,CreationDate,VSTSLink,Tags,Categories):
    self.Description = Description
    self.Url = Url
    self.CreationDate = CreationDate   
    self.VSTSLink = VSTSLink
    self.Tags = Tags  
    self.Categories = Categories 
        

class SectionContentClass:
  '''This is SectionContentclass with ScenarioName, Description,Docs,Gaps as Parameters'''
  def __init__(self, ScenarioName,Description,Docs,Gaps):
    self.ScenarioName = ScenarioName
    self.Description = Description
    self.Docs = Docs
    self.Gaps=Gaps


class ContentClass:
  '''This is Content class with SectionTitle,SectionContent as Parameters'''
  def __init__(self,SectionTitle,SectionContent):
    self.SectionTitle = SectionTitle
    self.SectionContent = SectionContent

  def get_sectiontitle_list(self,contentindex):
    '''This function retrieves the list of SectionTitle'''
    self.contentindex = contentindex
    sectionlist=[]
    for contentindex in range(len(Root.Content)):
      sectionlist.append(Root.Content[contentindex].SectionTitle)    
    return sectionlist    

class RootClass:
  '''This is Root  class with SchemaVersion,Title,Description.Content as Parameters'''
  def __init__(self, SchemaVersion,Title,Description,Content):
    self.SchemaVersion = SchemaVersion
    self.Title = Title
    self.Description = Description    
    self.Content = Content   
      
def class_mapper(d):
  return mapping[frozenset(d.keys())](**d)					  

d=  ''' 
       {
    "SchemaVersion": "2",
    "Title": "Title of the Application",
    "Description": "Description",
    "Content": [
      {
        "SectionTitle": "This is a Section_Title1",
        "SectionContent": [
          {
            "ScenarioName": "This is Scenario1 in Section_Title1",
            "Description": "Description of scenario",
            "Docs": [
              {
                "Name": "Scenario1_DocName1",
                "Link": "Scenario1_DocLink1"
              },
              {
                "Name": "Scenario1_DocName2",
                "Link": "Scenario1_DocLink2"
              }
            ],
            "Gaps": [
              {
                "Description": "Scenario1_Description of Gap1",
                "Url": "#",
                "CreationDate": "Jan",
                "VSTSLink": "#",
                "Tags": "Tags",
                "Categories": "Categories"
               
              },
              {
                "Description": "Scenario1_Other gap description",
                "Url": "#",
                "CreationDate": "Feb",
                "VSTSLink": "#",
                "Tags": "Tags",
                "Categories": "Categories"
                
              }
            ]
          },
          {
            "ScenarioName": "This is Scenario2 in Section_Title1",
            "Description": "Description of scenario2",
            "Docs": [
              {
                "Name": "Scenario2_DocName1",
                "Link": "Scenario1_DocLink1"
              },
              {
                "Name": "Scenario2_DocName2",
                "Link": "Scenario2_DocLink2"
              }
            ],
            "Gaps": []
          },
          {
            "ScenarioName": "This is Scenario3 in Section_Title1",
            "Description": "Description of Scenario3",
            "Docs": [
              {
                "Name": "Scenario3_DocName1",
                "Link": "Scenario2_DocLink1"
              }
            ],
            "Gaps": []
          }
        ]
      },
      {
        "SectionTitle": "This is Section_Title2",
        "SectionContent": [
          {
            "ScenarioName": "This is Scenario1 in Section_Title2",
            "Description": "Description of Scenario1",
            "Docs": [
              {
                "Name": "Scenario1_DocName1",
                "Link": "Scenario1_DocLink1"
              }
            ],
            "Gaps": []
          },
          {
            "ScenarioName": "This is Scenario2 in Section_Title2",
            "Description": "Description of Scenario2",
            "Docs": [
              {
                "Name": "Scenario2_DocName1",
                "Link": "Scenario2_DocLink1"
              }
            ],
            "Gaps": []
          }
        ]
      }
    ]
  }
'''
mapping = {frozenset(('Name', 
                      'Link')): DocsClass,
           frozenset(('Description',
                       'Url',
                       'CreationDate',
                       'VSTSLink',
                        'Tags',
                        'Categories')):GapsClass,         
           frozenset(('ScenarioName', 
                      'Description',
                      'Docs','Gaps')): SectionContentClass,
            frozenset(('SectionTitle',
                       'SectionContent')):ContentClass,
            frozenset(('SchemaVersion',
                       'Title',
                       'Description',
                       'Content')):RootClass           
                      }     

Root = json.loads(d, object_hook=class_mapper)
#ContentObject=ContentClass.get_sectiontitle_list()

def main():
    '''Main method '''
    sectionlist=[]
    for i in range(len(Root.Content)):
        sectionlist.append(Root.Content[i].SectionTitle)
    print(sectionlist)
if __name__ == '__main__':
    main()

