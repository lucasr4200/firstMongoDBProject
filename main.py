import datetime

from pymongo import MongoClient
from datetime import date


client = MongoClient()

db = client["test"]

data = [{"abstract": "The purpose of this study is to develop a learning tool for high school students studying the scientific aspects of information and communication net- works. More specifically, we focus on the basic principles of network proto- cols as the aim to develop our learning tool. Our tool gives students hands-on experience to help understand the basic principles of network protocols.", "authors": ["Makoto Satoh", "Ryo Muramatsu", "Mizue Kayama", "Kazunori Itoh", "Masami Hashimoto", "Makoto Otani", "Michio Shimizu", "Masahiko Sugimoto"], "n_citation": 0, "references": ["51c7e02e-f5ed-431a-8cf5-f761f266d4be", "69b625b9-ebc5-4b60-b385-8a07945f5de9"], "title": "Preliminary Design of a Network Protocol Learning Tool Based on the Comprehension of High School Students: Design by an Empirical Study Using a Simple Mind Map", "venue": "international conference on human-computer interaction", "year": 2013, "id": "00127ee2-cb05-48ce-bc49-9de556b93346"},
{"abstract": "This paper describes the design and implementation of a methodology for the visualisation and hypothetical virtual reconstruction of Roman polychrome statuary for research purposes. The methodology is intended as an attempt to move beyond visualisations which are simply believable towards a more physically accurate approach. Accurate representations of polychrome statuary have great potential utility both as a means of illustrating existing interpretations and as a means of testing and revising developing hypotheses. The goal of this methodology is to propose a pipeline which incorporates a high degree of physical accuracy whilst also being practically applicable in a conventional archaeological research setting. The methodology is designed to allow the accurate visualisation of surviving objects and colourants as well as providing reliable methods for the hypothetical reconstruction of elements which no longer survive. The process proposed here is intended to limit the need for specialist recording equipment, utilising existing data and those data which can be collected using widely available technology. It is at present being implemented as part of the 'Statues in Context' project at Herculaneum and will be demonstrated here using the case study of a small area of the head of a painted female statue discovered at Herculaneum in 2006.", "authors": ["Gareth Beale", "Graeme Earl"], "n_citation": 50, "references": ["10482dd3-4642-4193-842f-85f3b70fcf65", "3133714c-f979-4d84-9224-97361cf053ab", "3a926fef-7422-4654-8776-8e31b45be563", "52f480e8-85e6-4c01-9e5b-d75eabf6a8ec", "6f52f995-7c4c-4a92-83aa-d1c9fbd2465c", "8bd964d6-c45f-448c-9e65-efe5f98ca0a0", "8fa0a362-6522-48fc-bd5e-24de00ed6511", "9bfa8c24-8fb6-44d9-ba42-38b22f9cf34b", "b57cc9ef-64b6-479d-9918-5f283af3219d", "b678b546-e867-4a57-8963-c5545b04f32d", "e5c40bf5-7ee2-4cff-a75a-b708ab69997b", "f0dccb0c-c17a-4fcb-a89f-fe4bdfa3356d", "fdd93623-31c8-487b-8554-d6c6b25af5f6"], "title": "A methodology for the physically accurate visualisation of roman polychrome statuary", "venue": "visual analytics science and technology", "year": 2011, "id": "001c58d3-26ad-46b3-ab3a-c1e557d16821"},
{"abstract": "This article applied GARCH model instead AR or ARMA model to compare with the standard BP and SVM in forecasting of the four international including two Asian stock markets indices.These models were evaluated on five performance metrics or criteria. Our experimental results showed the superiority of SVM and GARCH models, compared to the standard BP in forecasting of the four international stock markets indices.", "authors": ["Altaf Hossain", "Faisal Zaman", "Mohammed Nasser", "M. Mufakhkharul Islam"], "n_citation": 50, "references": ["2d84c0f2-e656-4ce7-b018-90eda1c132fe", "a083a1b9-8dfb-45d6-99a9-fa30c4a6e9f5"], "title": "Comparison of GARCH, Neural Network and Support Vector Machine in Financial Time Series Prediction", "venue": "pattern recognition and machine intelligence", "year": 2009, "id": "001c8744-73c4-4b04-9364-22d31a10dbf1"},
{"abstract":None,"authors": ["Jea-Bum Park", "Byungmok Kim", "Jian Shen", "Sun-Young Kim", "Dae-Seok Rho"], "n_citation": 0, "references": ["8c78e4b0-632b-4293-b491-85b1976675e6", "9cdc54f0-f1a0-4422-ac16-d9164d9371ee"], "title": "Development of Remote Monitoring and Control Device for 50KW PV System Based on the Wireless Network", "venue": "", "year": 2011, "id": "00338203-9eb3-40c5-9f31-cbac73a519ec"},
{"abstract":None,"authors": ["Giovanna Guerrini", "Isabella Merlo"], "n_citation": 2, "title": "Reasonig about Set-Oriented Methods in Object Databases.", "venue": "", "year": 1998, "id": "0040b022-1472-4f70-a753-74832df65266"},
{"abstract":None,"authors": ["Rafael \u00c1lvarez", "Leandro Tortosa", "Jos\u00e9-Francisco Vicent", "Antonio Zamora"], "n_citation": 0, "title": "COMPARING GNG3D AND QUADRIC ERROR METRICS METHODS TO SIMPLIFY 3D MESHES", "venue": "international conference on computer graphics theory and applications", "year": 2009, "id": "005ce28f-ed77-4e97-afdc-a296137186a1"},
{"abstract":None,"authors": ["Jovan Dj. Golic", "Guglielmo Morgari"], "n_citation": 2, "title": "Vectorial fast correlation attacks.", "venue": "", "year": 2004, "id": "3fcd7cdc-20e6-4ea3-a41c-db126fcc5cfe"},
{"abstract":None,"authors": ["Guzin Ulutas", "Mustafa Ulutas", "Vasif V. Nabiyev"], "n_citation": 0, "references": ["5626736c-e434-4e2d-8405-54940fab88ab", "8e87e87b-87a8-4dd2-8365-e79fbe1b4b93", "98f543e3-d61c-4099-ae96-237816472592", "99e7103c-1f1c-4ac6-8cb1-e0af35606848"], "title": "Improved Secret Image Sharing Method By Encoding Shared Values With Authentication Bits", "venue": "international symposium on computer and information sciences", "year": 2011, "id": "00701b05-684f-45f9-b281-425abfec482c"},
{"abstract":None,"authors": ["Pranay Chaudhuri", "Hussein Thompson"], "n_citation": 0, "title": "A Self-Stabilizing Algorithm for Finding the Cutting Center of a Tree.", "venue": "parallel and distributed processing techniques and applications", "year": 2003, "id": "00745041-3636-4d18-bbec-783c4278c40d"},
{"abstract":None,"authors": ["Dominik Szajerman", "Adam Jurczy\u0144ski"], "n_citation": 0, "references": ["3fcd7cdc-20e6-4ea3-a41c-db126fcc5cfe", "bf3a11ca-5c4b-4b26-9b7a-0881b8d0f6c2"], "title": "Fur Visualisation for Computer Game Engines and Real-Time Rendering", "venue": "international conference on computer vision and graphics", "year": 2014, "id": "00964544-cbe2-4da9-bb5a-03333160eb34"}
]


collection = db["collection"]

# collection.delete_many({})
#
# lab_data = collection.insert_many(data)



# q2()

def artist_search():
       l = []
       lst = []
       n = int(input("Enter number of keywords:"))
       for i in range(n):
          k = input("enter keyword:")
          j=k.isnumeric()
          if j == True:
              k = int(k)
              q = {"year":k}
              z =collection.find(q)
              for j in z:
                  lst.append([j["abstract"],j["title"],j["authors"],j["venue"],j["year"]])
          else:
            l.append(k)



       print(l)

       for i in l:


            res = {"$or": [{"title":{"$regex":i,"$options": "i"}},{"venue":{"$regex":i,"$options": "i"}},
                     {"abstract":{"$regex":i,"$options": "i"}},{"authors":{"$regex":i,"$options": "i"}}
                           ]}
            x = collection.find(res)

            for r in x:

              lst.append([r["abstract"],r["title"],r["authors"],r["venue"],r["year"]])

       nlst = []
       for l in lst:
           # print(l[1])
           if l in nlst:
               pass
           else:
               nlst.append(l)


       s = '-'
       print(100 * s)
       for i in nlst:

          print(i)
          print(100 * s)
       if len(nlst)>0:
           articleSelected = input("Which title would you like to select?: ")
           article_select(articleSelected)


# test()

def article_select(articleSelected):
    query = {"title": articleSelected}
    x = collection.find(query)
    ref = []
    for i in x:


        print("title of article:", i['title'])
        print("abstract of article:", i["abstract"])
        print("reference of article:", i["references"])
        print("year:", i['year'])
        print("venue:", i['venue'])

        print("--------")
        if len(i["references"])>0:
            for re in i["references"]:
                ref.append(re)

    y = collection.find()
    # print(y)
    print("_______REFERENCES_______")

    for f in y:
        for p in ref:
            if f["id"] == p:
                print("id:", f['id'])
                print("title of article:", f['title'])
                print("abstract of article:", f["abstract"])
                print("year:", f['year'])
                print("_______")


def add():
    id = int(input("enter unique id:"))
    title = input("Enter title:")
    authors_lst = []
    n = int(input("Enter number of authors:"))
    for i in range(n):
        author = input("enter author name:")
        authors_lst.append(author)
    today = datetime.datetime.now()
    year = today.year
    abstract = None
    venue = None
    ref = []
    citations = 0
    list = {"abstract": None, "authors": authors_lst, "n_citation": 0,
             "references": [],
             "title": title, "venue": None,
             "year": year, "id": id}
    z = collection.insert_one(list)






# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # add()
    artist_search()

