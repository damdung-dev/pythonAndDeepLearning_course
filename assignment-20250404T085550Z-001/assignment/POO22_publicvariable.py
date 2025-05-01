class Experience:
    count=0
    listBirthDate_exp = []
    listCandidateId_exp = []
    listFirstName_exp = []
    listLastName_exp = []
    listAddress_exp = []
    listPhone_exp = []
    listEmail_exp = []
    listCandidateType_exp = []
    listExpInyear_exp = []
    listProSkill_exp = []
    def __init__(self,FirstName,LastName,BirthDate,Address,Phone,Email,Candidatetype,ExpInYear,ProSkill):
        Experience.count += 1
        self.candidateId=Experience.count
        self.FirstName = FirstName
        self.LastName = LastName
        self.BirthDate = BirthDate
        self.Address = Address
        self.Phone = Phone
        self.Email = Email
        self.Candidatetype = Candidatetype
        self.ExpInYear = ExpInYear
        self.ProSkill = ProSkill
    #---------------------Methods
    #def create_exp_candidate(self):
    def create_expCandidate(self):
        Experience.listFirstName_exp.append(self.FirstName)
        Experience.listLastName_exp.append(self.LastName)
        Experience.listBirthDate_exp.append(self.BirthDate)
        Experience.listAddress_exp.append(self.Address)
        Experience.listPhone_exp.append(self.Phone)
        Experience.listEmail_exp.append(self.Email)
        Experience.listCandidateType_exp.append(self.Candidatetype)
        Experience.listExpInyear_exp.append(self.ExpInYear)
        Experience.listProSkill_exp.append(self.ProSkill)
        CandidateManagementSystem.continueDisplay("continuedisplay")
        print(Experience.listFirstName_exp,Experience.listLastName_exp)
class Fresher(Experience):
    listBirthDate_fre = []
    listCandidateId_fre = []
    listFirstName_fre = []
    listLastName_fre = []
    listAddress_fre = []
    listPhone_fre = []
    listEmail_fre = []
    listCandidateType_fre = []
    listExpInyear_fre = []
    listProSkill_fre = []
    count = 0
    def __init__(self,FirstName,LastName,BirthDate,Address,Phone,
                 Email,Candidatetype,Graduation_date,Graduation_rank,Education):
        Fresher.count += 1
        self.candidateId =Fresher.count
        self.Graduation_date = Graduation_date
        self.Graduation_rank = Graduation_rank
        self.Education = Education
        super().__init__(FirstName,LastName,BirthDate,Address,Phone,
                 Email,Candidatetype,ExpInYear=0,ProSkill=" ")

    def create_freCandidate(self):
        Fresher.listFirstName_fre.append(self.FirstName)
        Fresher.listLastName_fre.append(self.LastName)
        Fresher.listBirthDate_fre.append(self.BirthDate)
        Fresher.listAddress_fre.append(self.Address)
        Fresher.listPhone_fre.append(self.Phone)
        Fresher.listEmail_fre.append(self.Email)
        Fresher.listCandidateType_fre.append(self.Candidatetype)
        Fresher.listExpInyear_fre.append(self.ExpInYear)
        Fresher.listProSkill_fre.append(self.ProSkill)
class Intern(Experience):
    listBirthDate_intern = []
    listCandidateId_intern = []
    listFirstName_intern = []
    listLastName_intern = []
    listAddress_intern = []
    listPhone_intern = []
    listEmail_intern = []
    listCandidateType_intern = []
    listExpInyear_intern = []
    listProSkill_intern = []
    count = 0
    def __init__(self,FirstName,LastName,BirthDate,
                 Address,Phone,Email,Candidatetype,Majors, Semester, Universityname):
        Intern.count += 1
        self.__candidateId = Intern.count
        self.__Majors = Majors
        self.__Semester = Semester
        self.__Universityname = Universityname
        self.__Candidatetype = Candidatetype
        super().__init__(FirstName, LastName, BirthDate, Address, Phone,Email, Candidatetype,ExpInYear=0,ProSkill=" ")
    def create_internCandidate(self):
        Intern.listFirstName_intern.append(self.FirstName)
        Intern.listLastName_intern.append(self.LastName)
        Intern.listBirthDate_intern.append(self.BirthDate)
        Intern.listAddress_intern.append(self.Address)
        Intern.listPhone_intern.append(self.Phone)
        Intern.listEmail_intern.append(self.Email)
        Intern.listCandidateType_intern.append(self.Candidatetype)
        Intern.listExpInyear_intern.append(self.ExpInYear)
        Intern.listProSkill_intern.append(self.ProSkill)

class CandidateManagementSystem:
    listRank=["Excellence","Good","Fair","Poor"]
    def mainScreen(self):
        print("CANDIDATE MANAGEMENT SYSTEM\n\t 1. Experience \n\t 2. Fresher "
              "\n\t 3. Internship \n\t 4. Searching \n\t 5. Exit")
        user=input("Please choose one of the options above: ")
        if user=="1":
            CandidateManagementSystem.experience_method("exp")
        elif user=="2":
            CandidateManagementSystem.fresher_method("fre")
        elif user=="3":
            CandidateManagementSystem.intern_method("intern")
        elif user=="4":
            CandidateManagementSystem.search_method("search")
        else:
            exit()
    def experience_method(self):
        Candidatetype = 0
        print(f"CREATE A NEW EXPERIENCE CANDIDATE")
        FirstName = input("\tFirst Name: ")
        LastName = input("\tLast Name: ")
        BirthDate = input("\tBirthday: ")
        Phone = input("\tPhone: ")
        Address = input("\tAddress: ")
        Email = input("\tEmail: ")
        YearOfExperience = int(input("\tYear Of Experience: "))
        RankOfGraduation = input("\tRank Of Graduation (Excellence, Good, Fair, Poor): ")
        ProSkill = input("\tProfessional skills: ")
        if len(BirthDate) == 4 and BirthDate.isdigit() == True:
            if len(Phone) >= 10 and Phone.isdigit() == True:
                if RankOfGraduation in CandidateManagementSystem.listRank:
                    if Email.find('@') != -1:
                        candidate1 = Experience(FirstName, LastName, BirthDate, Address, Phone, Email,
                                                Candidatetype, YearOfExperience, ProSkill)
                        candidate1.create_expCandidate()
                    else:
                        print("Error! Please check your mail again")
                        system=CandidateManagementSystem()
                        system.mainScreen()
                else:
                    print("Error! Please check your rank graduation again."
                          "\nThere are only 4 ranks: Excellence, Good, Fair, Poor")
                    system=CandidateManagementSystem()
                    system.mainScreen()
            else:
                print("Error! Please check your phone number again")
                system=CandidateManagementSystem()
                system.mainScreen()
        else:
            print("Error! Please check your birth date again.\nYou only need to type your year of birth")
            system=CandidateManagementSystem()
            system.mainScreen()

    def fresher_method(self):
        print(f"CREATE A NEW FRESHER CANDIDATE")
        Candidatetype = 1
        FirstName = input("\tFirst Name: ")
        LastName = input("\tLast Name: ")
        BirthDate = input("\tBirthday: ")
        Phone = input("\tPhone: ")
        Address = input("\tAddress: ")
        Email = input("\tEmail: ")
        GraduationDate = input("\tGraduation date: ")
        RankOfGraduation = input("\tRank Of Graduation (Excellence, Good, Fair, Poor): ")
        Education = input("\tWhere did you graduate: ")
        if len(BirthDate) == 4 and BirthDate.isdigit() == True:
            if len(Phone) >= 10 and Phone.isdigit() == True:
                if RankOfGraduation in CandidateManagementSystem.listRank:
                    if Email.find('@') != -1:
                        candidate2 = Fresher(FirstName, LastName, BirthDate, Address, Phone, Email, Candidatetype,
                                             GraduationDate, RankOfGraduation, Education)
                        candidate2.create_freCandidate()
                    else:
                        print("Error! Please check your mail again")
                        system = CandidateManagementSystem()
                        system.mainScreen()
                else:
                    print("Error! Please check your rank graduation again."
                          "\nThere are only 4 ranks: Excellence, Good, Fair, Poor")
                    system = CandidateManagementSystem()
                    system.mainScreen()
            else:
                print("Error! Please check your phone number again")
                system = CandidateManagementSystem()
                system.mainScreen()
        else:
            print("Error! Please check your birth date again.\nYou only need to type your year of birth")
            system = CandidateManagementSystem()
            system.mainScreen()
    def intern_method(self):
        print(f"CREATE A NEW INTERN CANDIDATE")
        Candidatetype = 1
        FirstName = input("\tFirst Name: ")
        LastName = input("\tLast Name: ")
        BirthDate = input("\tBirthday: ")
        Phone = input("\tPhone: ")
        Address = input("\tAddress: ")
        Email = input("\tEmail: ")
        Major=input("\tYour major: ")
        Semester=input("\tSemester: ")
        Uniname=input("\tUniversity name: ")
        RankOfGraduation = input("\tRank Of Graduation (Excellence, Good, Fair, Poor): ")
        if len(BirthDate) == 4 and BirthDate.isdigit() == True:
            if len(Phone) >= 10 and Phone.isdigit() == True:
                if RankOfGraduation in CandidateManagementSystem.listRank:
                    if Email.find('@') != -1:
                        candidate3 = Intern(FirstName, LastName, BirthDate, Address, Phone, Email, Candidatetype,
                                             Major,Semester,Uniname)
                        candidate3.create_internCandidate()
                    else:
                        print("Error! Please check your mail again")
                        system = CandidateManagementSystem()
                        system.mainScreen()
                else:
                    print("Error! Please check your rank graduation again."
                          "\nThere are only 4 ranks: Excellence, Good, Fair, Poor")
                    system = CandidateManagementSystem()
                    system.mainScreen()
            else:
                print("Error! Please check your phone number again")
                system = CandidateManagementSystem()
                system.mainScreen()
        else:
            print("Error! Please check your birth date again.\nYou only need to type your year of birth")
            system = CandidateManagementSystem()
            system.mainScreen()
    def search_method(self):
        firstNameSearch=input("Please input Your first Name: ")
        lastNameSearch=input("Please input Your last Name: ")
        CandidatetypeSearch=input("Please input Your Candidatetype: ")
        for dem1 in range(0,len(Experience.listFirstName_exp)):
            print(Experience.listFirstName_exp[dem1], end=" ")
        for dem2 in range(0,len(Experience.listLastName_exp)):
            print(Experience.listFirstName_exp[dem2])
        for dem3 in range(0,len(Fresher.listFirstName_fre)):
            print(Fresher.listLastName_exp[dem3],end=" ")
        for dem4 in range(0,len(Fresher.listLastName_fre)):
            print(Fresher.listLastName_fre[dem4])
        for dem5 in range(0,len(Intern.listFirstName_intern)):
            print(Experience.listLastName_exp[dem5], end=" ")
        for dem6 in range(0,len(Intern.listFirstName_intern)):
            print(Intern.listFirstName_intern[dem6])
    def continueDisplay(self):
        user=input("Do you want to continue? \n1.Yes \n2.No")
        if user == "1":
            CandidateManagementSystem.mainScreen("mainScreen")
if __name__=="__main__":
    system=CandidateManagementSystem()
    system.mainScreen()
