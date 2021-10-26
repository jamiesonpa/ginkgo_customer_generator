from os import write
import random
import time
import streamlit as st


def generate_size(size_breakdown):

    micro = size_breakdown[0]
    small = size_breakdown[1]
    mid = size_breakdown[2]
    large = size_breakdown[3]

    sizes = [("a",micro), ("b", small), ("c", mid), ("d",large)]
    size_choice_matrix = []
    for size in sizes:
        counter = 0
        while counter < size[1]:
            size_choice_matrix.append(size[0])
            counter+=1
        
    size_choice_letter = random.choice(size_choice_matrix)
    if size_choice_letter == "a":
        size = random.randint(1000000,20000000)
    elif size_choice_letter == "b":
        size = random.randint(20000000,100000000)
    elif size_choice_letter == "c":
        size = random.randint(100000000,1000000000)
    elif size_choice_letter == "d":
        size = random.randint(1000000000,100000000000)
    return size

def generate_name():

    lastnameconjugateprobabilitypercentage = 10
    islastnameconj = False

    randint = random.randint(1,100)
    if randint > (99-lastnameconjugateprobabilitypercentage):
        islastnameconj = True


    if islastnameconj == False:
        with open("prefixes.txt") as readfile:
            prefixes = readfile.read().split("\n")
            fixed_prefixes = []
            for prefix in prefixes:
                # prepref = prefix[0:len(prefix)]
                endings = ["e","a","o","i","y"]
                vowel_found = False
                for end in endings:
                    if prefix[-1] == end:
                        vowel_found = True

                if vowel_found == True:
                    newprefix = prefix.capitalize()
                    newprefix = newprefix.replace("oo","o")
                    fixed_prefixes.append(newprefix)
                else:
                    prepref = prefix[0:len(prefix)]
                    newprefix = prepref +random.choice(endings)
                    newprefix = newprefix.replace("oo","o")
                    fixed_prefixes.append(newprefix.capitalize())
            prefixes = fixed_prefixes

        with open("suffixes.txt") as readfile:
            suffixes = readfile.read().split("\n")
            readfile.close()

        random_name = random.choice(prefixes) + random.choice(suffixes)
        random_name = random_name.replace("oo","o")
        random_name = random_name.replace("aa","a")
        random_name = random_name.replace("yy","y")
        random_name = random_name.replace("uu","u")
        random_name = random_name.replace("ii","i")


        return random_name
    else:
        with open("lastnames.txt") as readfile:
            lastnames = readfile.read().split("\n")
            lastname1 = random.choice(lastnames)
            lastname2 = random.choice(lastnames)
            random_name = lastname1 + " & " + lastname2
        return random_name

def generate_description(name, industry):
    #pharma
    if industry == "Biopharma":
        with open("diseases.txt") as readfile:
            diseases = readfile.read().split("\n")
            readfile.close()
        terms0 = ["ultracompact ","L-enantiomeric ","R-enantiomeric ","novel mode-of-action ","clinically-tested ","immunogenic ","tumor-infiltrating ","","",""]
        terms1 = ["antisense oligos", "vaccine adjuvants","aptamers","vaccines","gene-therapies","lipid nanoparticles","virus-like particles","monoclonal antibodies", "protein kinase inhibitors", "naturally occuring immunosuppressive molecules", "viral coat proteins","antimicrobial peptides","small molecule therapeutics"]
        description = name + " is a company known for manufacturing " +random.choice(terms0) + random.choice(terms1) + " for the treatment of " + random.choice(diseases).lower() + ". However, they would like to begin manufacturing these therapeutics on a cellular platform."

    #indu/env

    if industry == "Industrial/Environmental":
        terms1 = ["phytoremediation", "environmental cleanup", "direct-air carbon capture", "climate change","water purification"]
        terms2 = ["bioengineering", "biomechatronics", "ESG-conscious corporate architecture", "biosensors", "first principles engineering", "biohacking","in silico biology", "artificial intelligence", "blockchain", "drone imaging", "ai-enabled analytics", "protein-protein interaction predictions", "molecular modelling"]
        terms3 = ["tackle", "solve","monetize","revolutionize indstry-wide approaches to","understand"]
        description = name + " is a company that is trying to " +random.choice(terms3)+" the age-old problem of " + random.choice(terms1) + " using a unique approach to " + random.choice(terms2)+". They would like Ginkgo to help them develop their new product using cell engineering."
    #agbio
    if industry == "Agricultural Biology":
        regions = ["rhizosphere","phytosphere","plant holobiome"]
        microbetypes = ["viruses", "viroids","bacteria","protozoa","fungi","oomycetes"]
        plant_types = ["monocot","dicot"]
        enhance_protect = ["enhance plant growth", "enhance plant immunity"]

        description = name + " is an AgBio company focused on developing " + random.choice(regions) + "-associating " + random.choice(microbetypes) + " that can " + random.choice(enhance_protect) + " in economically-relevant " + random.choice(plant_types) + " crop species. They would like Ginkgo to help with that."
    #consumertech
    if industry == "Consumer Technology":
        adjectives = ["incredible", "low-cost", "artisanal", "hand-crafted", "heirloom","authentic","best-in-class","world-renown"]
        sizzler = ["organic", "non-gmo", "ethically-sourced", "locally grown", "gluten-free","lactose-free","hypoallergenic", "all-natural"]
        products = ["mobile phones", "perfume", "eyeshadow", "lipstick", "shampoo", "hairspray", "eye drops", "yoga mats", "microscope filters"]
        description = name + " is a consumer tech company that is known for their "+ random.choice(adjectives) + " " + random.choice(sizzler) + " " + random.choice(products) + ". They would like Ginkgo to help them develop cell lines for a new product suite."


    #food
    if industry == "Food/Beverage":
        sizzler = ["organic", "non-gmo", "ethically-sourced", "locally grown", "gluten-free","lactose-free","hypoallergenic", "all-natural"]
        products = ["hamburgers", "breast milk", "meatballs", "chibben tendies","beer", "kombucha","french fries", "meal replacement shakes","cookies"]
        description = name + " is a food and beverage company that is trying to develop microbially-produced " + random.choice(sizzler) + " " + random.choice(products)+". They are hoping Ginkgo will help them figure out some issues they're having."
        pass
    #defense
    if industry == "Defense":
        sizzler = ["nuclear powered","solar powered","thermally resistant", "adaptive, armor plated", "bullet-proof", "nanobot-containing", "advanced", "ballistic", "subsonic", "stealth", "hypersonic", "suborbital", "geostationary"]
        products = ["film coatings", "bullets", "explosives", "fuel", "body armor","tanks", "sniper rifles",  "precision lasers", "grenades", "napalm", "UAVs","missiles","attack drones"]
        description = name + " is a defense company that is trying to develop microbially-produced " + random.choice(sizzler) + " " + random.choice(products)+". They are hoping Ginkgo will help them figure out some issues they're having."

    return description

def generate_industry(name, industry_breakdown):
    consumer_tech = industry_breakdown[0]
    indu_envi = industry_breakdown[1]
    ag = industry_breakdown[2]
    food = industry_breakdown[3]
    pharma = industry_breakdown[4]
    defense = industry_breakdown[5]

    industries = [("Consumer Technology",consumer_tech), ("Industrial/Environmental", indu_envi), ("Agricultural Biology", ag), ("Food/Beverage",food), ("Biopharma" ,pharma), ("Defense",defense)]
    choicematrix = []
    for indu in industries:
        counter = 0
        while counter < indu[1]:
            choicematrix.append(indu[0])
            counter+=1
    
    industry = random.choice(choicematrix)

    pharmachoices = [" Biopharma"," Pharmaceuticals"," Therapeutics"," Oncology"," Labs","",""]
    if industry == "Biopharma":
        if name.find(" ") != -1:
            newname = name.split(" ")[0] + random.choice(pharmachoices)
        else:
            newname = name + random.choice(pharmachoices)

    foodchoices = [" Foods"," FoodWorks"," Nutrition"," FoodLabs","",""]
    if industry == "Food/Beverage":
        if name.find(" ") != -1:
            newname = name.split(" ")[0] + random.choice(foodchoices)
        else:
            newname = name + random.choice(foodchoices)

    tech = [" Technologies"," Network"," Devices"," Labs"," Systems","",""]
    if industry == "Consumer Technology":
        if name.find(" ") != -1:
            newname = name.split(" ")[0] + random.choice(tech)
        else:
            newname = name + random.choice(tech)

    if industry == "Industrial/Environmental":
        if name.find(" ") != -1:
            newname = name.split(" ")[0] + random.choice(tech)
        else:
            newname = name + random.choice(tech)
        
    defen = [" Defense Solutions"," Tactical"," Defense"," Dynamics Corp."," Systems"," Dynamics","", ""]
    if industry == "Defense":
        if name.find(" ") != -1:
            newname = name.split(" ")[0] + random.choice(defen)
        else:
            newname = name + random.choice(defen)

    ag = [" Ag"," Bio", " Crop Science"," Farms","", ""]
    if industry == "Agricultural Biology":
        if name.find(" ") != -1:
            newname = name.split(" ")[0] + random.choice(ag)
        else:
            newname = name + random.choice(ag)


    return (industry,newname)

def generate_project(industry, size,type_risk_breakdown):
    
    project_types = ["Protein Overexpression", "Protein Overexpression", "Protein Overexpression", "Heterologous Biosynthetic Pathway Engineering", "Cell Line Optimization", "Microbiome Treatment", "Living Therapy"]
    project_type_risks = []
    for projtype in project_types:
        if projtype == "Protein Overexpression":
            project_type_risks.append(1-type_risk_breakdown[0])
        if projtype == "Heterologous Biosynthetic Pathway Engineering":
            project_type_risks.append(1- type_risk_breakdown[1])
        if projtype == "Cell Line Optimization":
            project_type_risks.append(1-type_risk_breakdown[2])
        if projtype == "Microbiome Treatment":
            project_type_risks.append(1-type_risk_breakdown[3])
        if projtype == "Living Therapy":
            project_type_risks.append(1-type_risk_breakdown[4])

    organism_types = ["HEK293","CHO","yeast","E. coli","yeast","E. coli","yeast","E. coli","Alternative Bacterium","Alternative Fungus","Alternative Bacterium","Alternative Fungus","Alternative Bacterium","Alternative Fungus"]
    difficulties = ["easy","intermediate","hard"]

    #defining organism attributes
    #organism name, doubling time in minutes, sterility reqs (3 is highest, 2 is intermediate, 1 is lowest, 
    # transformation difficulty (same scale), 
    # genome size (megabases), 
    # genome annotation patchiness factor (same scale as others))
    # handling difficulty (same scale as others)
    hek293 = {}
    hek293["name"] = "HEK293"
    hek293["domain"] = "eukaryote"
    hek293["doubling time"] = 2000
    hek293["sterility reqs"] = difficulties[2]
    hek293["td"] = difficulties[2]
    hek293["genome size"] = 3200
    hek293["gapf"] = difficulties[0]
    hek293["hd"] = difficulties[2]
    #diffrisk is an average of normalized difficulty ratings (each easy rating and makes it 3, intermediate 6, and hard 9), doubling time difficulty rating ((dbling time /2000)*10)
    hek293["diffrisk"] = (((9+3+9+9+10)/5)*10)

    cho = {}
    cho["name"] = "Chinese Hamster Ovary"
    cho["domain"] = "eukaryote"
    cho["doubling time"] = 1440
    cho["sterility reqs"] = difficulties[2]
    cho["td"] = difficulties[2]
    cho["genome size"] = 2790
    cho["gapf"] = difficulties[0]
    cho["hd"] = difficulties[2]
    cho["diffrisk"] = (((9+3+9+9+(10*(1440/2000)))/5)*10)

    ecoli = {}
    ecoli["name"] = "E. coli"
    ecoli["domain"] = "prokaryote"
    ecoli["doubling time"] = 20
    ecoli["sterility reqs"] = difficulties[0]
    ecoli["td"] = difficulties[0]
    ecoli["genome size"] = 5.5
    ecoli["gapf"] = difficulties[0]
    ecoli["hd"] = difficulties[0]
    ecoli["diffrisk"] = (((3+3+3+3+(10*(20/2000)))/5)*10)

    yeast = {}
    yeast["name"] = "yeast"
    yeast["domain"] = "eukaryote"
    yeast["doubling time"] = 90
    yeast["sterility reqs"] = difficulties[1]
    yeast["td"] = difficulties[1]
    yeast["genome size"] = 12
    yeast["gapf"] = difficulties[0]
    yeast["hd"] = difficulties[0]
    yeast["diffrisk"] = (((3+3+6+6+(10*(90/2000)))/5)*10)


    organism_type = random.choice(organism_types)
    if organism_type == "HEK293":
        organism_choice = hek293
    elif organism_type == "CHO":
        organism_choice = cho
    elif organism_type == "E. coli":
        organism_choice = ecoli
    elif organism_type == "yeast":
        organism_choice = yeast
    elif organism_type == "Alternative Bacterium":
        letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        with open("bacterial_species_names.txt") as readfile:
            species_names = readfile.read().split("\n")
            readfile.close()
        
        species_name = random.choice(species_names)
        letter_name = random.choice(letters) + ". "
        random_bacterium = {}
        random_bacterium["name"] = letter_name + species_name
        random_bacterium["domain"] = "prokaryote"
        random_bacterium["doubling time"] = random.randint(20,60)
        choices1 = ["easy","intermediate"]
        dr1= random.randint(1,2)
        random_bacterium["sterility reqs"] = choices1[dr1-1]
        dr2= random.randint(1,2)
        random_bacterium["td"] = choices1[dr2-1]
        random_bacterium["genome size"] = random.randint(3,10)
        dr3 = random.randint(1,2)
        random_bacterium["gapf"] = choices1[dr3-1]
        random_bacterium["hd"] = "easy"
        random_bacterium["diffrisk"] = (((3*dr1)+(3*dr2)+(3*dr3)+3+(10*(random_bacterium["doubling time"]/2000)))/5)*10
        organism_choice = random_bacterium
    elif organism_type == "Alternative Fungus":
        letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        with open("fungal_species_names.txt") as readfile:
            species_names = readfile.read().split("\n")
            readfile.close()
        
        species_name = random.choice(species_names)
        letter_name = random.choice(letters) + ". "
        random_fungus = {}
        choices1 = ["easy","intermediate"]
        choices2 = ["intermediate","hard"]
        random_fungus["name"] = letter_name + species_name
        random_fungus["domain"] = "eukaryote"
        random_fungus["doubling time"] = random.randint(60,180)
        dr1 = random.randint(1,2)
        random_fungus["sterility reqs"] = choices1[dr1-1]
        dr2 = random.randint(1,2)
        random_fungus["td"] = choices1[dr2-1]
        random_fungus["genome size"] = random.randint(10,100)
        dr3 = random.randint(2,3)
        random_fungus["gapf"] = choices1[dr3-2]
        dr4 = random.randint(1,2)
        random_fungus["hd"] = choices1[dr4-1]
        random_fungus["diffrisk"] = (((3*dr1)+(3*dr2)+(3*dr3)+(3*dr4)+(10*(random_fungus["doubling time"]/2000)))/5)*10
        organism_choice = random_fungus
    else:
        st.write("couldnt find organism")
    

    project_type_int = random.randint(0,(len(project_types)-1))
    project_type = project_types[project_type_int]
    project_type_risk = project_type_risks[project_type_int]



    project = [organism_choice, project_type, project_type_risk]
    return project

def ginkgo_customer_generator(number_to_generate, industry_breakdown, size_breakdown, sizerisk_coeff, startup_risk_coeff,type_risk_breakdown,organism_difficulty_scalar,returning_customer_prob, returning_customer_risk_reduction_coeff):

    total_cash_payments = 0
    total_equity_compensations = []
    customer_results = []
    counter = 0
    while counter < number_to_generate:
        initial_name = generate_name() #get a random name
        industry_tuple = generate_industry(initial_name, industry_breakdown) #choose a random industry, and change name in feeded
        name = industry_tuple[1]
        industry = industry_tuple[0]

        descript = generate_description(name, industry) #make a random description
        size = generate_size(size_breakdown) #get a random size


        returning_customer = False #determine if this is a returning customer or not
        returning_customer_risk_coefficient = 1
        returning_customer_int = random.randint(1,100)
        if size > 50000000:
            if returning_customer_int >= 1-(returning_customer_prob*100):
                returning_customer = True
                returning_customer_risk_coefficient = returning_customer_risk_reduction_coeff

        project = generate_project(industry,size,type_risk_breakdown) #generate the project
        organism = project[0]
        specs = project[1]
        project_risk = project[2]
        

        #simulate the customer
        st.write("\n\n-----------------------SIMULATED CUSTOMER #" + str(counter+1)+"--------------------")
        st.write(name + " is a company in the " + industry + " industry. This company has a $" + "{:,}".format(size) + " market capitalization.\n")

        #here, we associate a risk with the size of the company. This is because companies which have fewer resources are less likely to be capable of scaling up the 
        #downstream application
        if size < 10000000:
            size_risk = (1 + sizerisk_coeff)
            startup_survival_probability = 1- (.6 * startup_risk_coeff)
        elif size < 100000000:
            size_risk = (1 + (sizerisk_coeff/2))
            startup_survival_probability = 1-(.6 * (startup_risk_coeff/2))
        elif size < 1000000000:
            size_risk = 1
            startup_survival_probability = 1
        else:
            size_risk = 1
            startup_survival_probability = 1
        

        #in case we want to add an industry risk
        industry_risk = 1

        if returning_customer == True:
            st.write(name + " has done business with Ginkgo before, and therefore the overall risk associated with this project is lower.\n")
        st.write(descript+"\n")
        adjusted_organism_difficulty_risk = 1-(1-organism["diffrisk"] * organism_difficulty_scalar)
        st.write("This company wants Ginkgo to use the organism " + organism["name"] + " for this project. " + organism["name"].capitalize() + " is a " + organism["domain"] + " with a doubling time of " + str(organism["doubling time"])+" minutes.\n")
        st.write(organism["name"].capitalize()+ " is an organism which has a " + organism["td"] + " transformation difficulty, has sterility requirements that make working with it in the lab " + organism["sterility reqs"] + ", has a genome annotation that makes working with it " + organism["gapf"]+", and because of how robust/weak it is in the face of shearing forces, handling it in the lab is " + organism["hd"]+".\n")
        st.write(organism["name"].capitalize() + ' has an associated ' + str(adjusted_organism_difficulty_risk) + r'% organism difficulty risk, where 100% is the highest risk rating and 0% is the lowest risk rating.' +"\n")
        st.write("The project is your basic " + specs.lower() + " type of thing. These kinds of projects have an associated " + str(project[2]) + '%' + " failure risk. \n")   

        overall_risk_num = (((project[2] + adjusted_organism_difficulty_risk)/2)*returning_customer_risk_coefficient*size_risk*industry_risk)
        overall_risk = str(round((((project[2] + adjusted_organism_difficulty_risk)/2)*returning_customer_risk_coefficient*size_risk*industry_risk),2))+"%"
        st.write("This project has approximately a " + overall_risk + " overall risk of failure.\n")

        failure_risk_modulus = 1
        simready = "y"
        # simready = input("Ready to simulate? (y/n):\n>")
        if simready.lower() == "y":
            st.write("Simulating project with " + name +", attempting to do " + project[1] + " in " + organism["name"])
            y1successful = False
            y2successful = False
            years = 0
            totalfailurecount = 0
            failurecount = 0
            while y1successful == False:
                if failurecount > 10:
                    failurecount = 9
                randomrating = (random.randint(totalfailurecount*2,1000)/10) * (1-(failurecount/failure_risk_modulus))
                #st.write("simulating phase 1 iteration, roll was " + str(round(randomrating,0)) + " -- trying to beat " + str(round(overall_risk_num,0)))
                if randomrating > overall_risk_num:
                    years = years + .5
                    st.write("Project year 1 successful. Project time elapsed = " +str(years*12) + " months...")
                    st.write("-----\n")
                    y1successful = True
                    failurecount = 0
                else:
                    years = years+.5
                    failurecount+=1
                    totalfailurecount +=1
                    #st.write("Setback occured. Project time elapsed = " +str(years*12) + " months...")
                if totalfailurecount > 20:
                    break
            
            while y2successful == False:
                if totalfailurecount > 20:
                    break
                if failurecount > 10:
                    failurecount = 9
                randomrating = (random.randint(totalfailurecount*2,1000)/10) * (1-(failurecount/failure_risk_modulus))
                #st.write("simulating phase 2 iteration, roll was " + str(round(randomrating,0)) + " -- trying to beat " + str(round(overall_risk_num,0)))

                if randomrating > overall_risk_num:
                    years = years + .5
                    st.write("Project year 2 objectives successful. Project time elapsed = " +str(years*12) + " months...")
                    y2successful = True
                else:
                    years = years+.5
                    failurecount +=1
                    totalfailurecount +=1
                    #st.write("Setback occured. Project time elapsed = " +str(years*12) + " months...")
                if totalfailurecount > 20:
                    break
                    
            if y1successful:
                projectfailure = True
                if y2successful:
                    projectfailure = False
                    st.write("Project successfully completed in " + str(years*12) + " months.")
            else:
                projectfailure = True
                st.write("This project completely failed resulting in " + str(years*12) + " months of wasted time")

            if projectfailure == False:
                st.write("Ginkgo delivered on their milestones and customer specifications.")
                #if it is a midcap company, we'll say there is a 50% chance that Ginkgo negotiated an equity agreement and 50% chance they negotiated cash
                cashonly = False
                if size_risk == 1.1:
                    cashchanceint = random.randint(1,100)
                    if cashchanceint > 50:
                        cashonly = True
                #if it is a largecap company, we'll say there is a 50% chance that Ginkgo negotiated an equity agreement and 50% chance they negotiated cash
                elif size_risk == 1:
                    cashonly = True
                else:
                #if it is a micro/small cap company, its a 0% chance that the negotiated revenue is cash.
                    cashonly = False
            
                #if the payment was negotiated to be cash, then we can estimate it was a payment worth 100,000,000-150,000,000 for a mid cap company, 200,000,000 for a large cap company
                cash_payment = 0
                if cashonly == True:
                    if size_risk == 1.1:
                        cash_payment = (random.randint(1,100)/100 * 50000000) + 100000000
                    if size_risk == 1:
                        cash_payment = (random.randint(1,100)/100 * 50000000) + 200000000
                    total_cash_payments = total_cash_payments + (cash_payment)
                    st.write(name + " compensated Ginkgo with a cash payment of $" + str(cash_payment))
                
                if cashonly == False:
                    #first check to see if this company just straight up fails
                    startup_survival_probability = (1-(startup_survival_probability*100))
                    startuprandint = random.randint(1,100)
                    if startup_survival_probability < startuprandint:
                        st.write("This company rolled high enough to not fail as a startup!")
                        cagr_negative = False
                    else:
                        st.write("Unfortunately, this startup failed before reaching 6 years.")
                        cagr_negative = True
                    if cagr_negative == False:
                        cagr = random.randint(0,50)/100
                    else:
                        cagr = random.randint(-5,-25)/100

                    
                    equity_comp = size*.15
                    st.write("This company has compensated Ginkgo for its services with $" + str(size*.15) + " worth of its equity, which has a " + str(cagr*100) + r"% CAGR")
                    total_equity_compensations.append((equity_comp,cagr))

            st.write("-----------------------SIMULATION COMPLETE-------------------")
            customer_data = []
            customer_data.append(name)
            customer_data.append(industry)
            customer_data.append("{:,}".format(size))
            if projectfailure == True:
                customer_data.append("FAIL")
            else:
                customer_data.append("SUCCESS")
            customer_data.append(str(years*12))
            customer_data.append(project[1])
            customer_data.append(organism["name"])
            customer_data.append(str(organism["diffrisk"])+"%")
            customer_data.append(overall_risk)
            counter+=1
            customer_results.append(customer_data)
            with open("customer_results.txt", "a") as writefile:
                for point in customer_data:
                    writefile.write(str(point)+",")
                writefile.write("\n")
                writefile.close()
    
    equity = 0
    wcagrsum = 0
    for equitypayment in total_equity_compensations:
        equity = equity + equitypayment[0]
        wcagrsum = wcagrsum + (equitypayment[0] * equitypayment[1])

    wcagrav = wcagrsum /len(total_equity_compensations)
    wcagr = wcagrav/equity

    
    st.write("This cohort of " + str(1) + " Ginkgo customers has resulted in a total of $" + str("{:,}".format(total_cash_payments))+" cash payments.")
    st.write("And a total of $" + str("{:,}".format(round(equity,2))) + " of equity which has a " +str((round(wcagr*100,2))) + "% CAGR.")





#we need to define important simulation inputs

# here we define the % composition breakdown of industry type by customer
defconsumertech = 19
definduenv = 21
defag = 18
deffoodag = 18
defpharma = 15
defdefense = 13


#here we define the % composition breakdown of company size for customer base in terms of market cap (millions)
defunder20 = 20
defunder100 = 60
defunder1000 = 15
defunder100000 = 5
#here we define a risk associated with the size of the company. This should be a number between 0 and 1 which 
#represents the risk associated with a smaller company. In other words, for two companies requesting the same project
#what do we estimate is the highest risk % associated with that smaller size due to resource constraints, default risk,
#lack of track record, etc. By defualt, I'll estimate that its 20% more risky to take on a smaller company as a partner
#compared to a larger company, so in that case I would set this to be 0.2

defsizerisk_coeff = 0.2

#let's assume that https://www.failory.com/blog/startup-failure-rate 60% of startups fail within the first five years
#if that is the case, then we can use that as the base case for whether the startup will fail or not and reduce from there based on
#1. the fact that Ginkgo is lending this startup its resources, and
#2. that Ginkgo has vetted this team's leadership and product potential itself
#with that in mind, define a coefficient to multiply this 45% by that will represent the risk reduction relative to a general startup
#caused by the association with Ginkgo

defstartup_risk_coeff = 0.5

#we also know that Ginkgo has some core competencies and proven track records depending on project type
#of these, we know protein overexpression, heterologous biosynthetic pathway engineering, cell line optimization, microbiome engineering, and living therapies are a few
#lets define % risk reduction relative base risk associated with each of these project types

defproteinexp = 40
defhetbiosynth = 25
defcelllineopt = 30
defmicrobiome = 20
deflivingtherapy = 10


#now, we have already decided a difficulty risk associated with each organism, but we should also add an input to determine how much weight the user would like
#to simulate organism difficulty as part of the simulation. We default to 1

deforganism_difficulty_scalar = 1

#if the customer is a returning customer, we would like to know, because that will change the risks associated.
#we want to define a probability that the customer is a returning customer, and we will default that to 30%

defreturning_customer_prob = .3

#and the associated reduction of total risk with returning customers should also be an input

defreturning_customer_risk_reduction_coeff = .66


st.title("Ginkgo Customer Generator")

st.sidebar.header("Inputs:\n")
st.sidebar.subheader("Customer Type Composition (must add up to 100)")
consumertech = st.sidebar.slider(label = "Consumer Tech%", min_value = 0, max_value=100, value =defconsumertech)
induenv = st.sidebar.slider(label = "Industrial/Environmental%", min_value = 0, max_value=100, value =definduenv)
ag = st.sidebar.slider(label = "Agricultural Biotech%", min_value = 0, max_value=100, value =defag)
foodag = st.sidebar.slider(label = "Food and Beverage%", min_value = 0, max_value=100, value =deffoodag)
pharma = st.sidebar.slider(label = "Pharmaceuticals%", min_value = 0, max_value=100, value =defpharma)
defense = st.sidebar.slider(label = "Defense%", min_value = 0, max_value=100, value =defdefense)

st.sidebar.subheader("Customer Size Composition (must add up to 100")
under20 = st.sidebar.slider(label = "Market Cap < $20,000,000 ", min_value = 0, max_value=100, value =defunder20)
under100 = st.sidebar.slider(label = "Market Cap < $100,000,000", min_value = 0, max_value=100, value =defunder100)
under1000 = st.sidebar.slider(label = "Market Cap < $1,000,000,000", min_value = 0, max_value=100, value =defunder1000)
under100000 = st.sidebar.slider(label = "Market Cap < $100,000,000,000", min_value = 0, max_value=100, value =defunder100000)

st.sidebar.subheader("Project Type Composition (must add up to 100")
proteinexp = st.sidebar.slider(label = "Protein Overexpression Optimization", min_value = 0, max_value=100, value =defproteinexp)
hetbiosynth = st.sidebar.slider(label = "Heterologous Expression of Biosynthetic Pathway", min_value = 0, max_value=100, value =defhetbiosynth)
celllineopt = st.sidebar.slider(label = "Cell Line Optimization", min_value = 0, max_value=100, value =defcelllineopt)
microbiome = st.sidebar.slider(label = "Microbiome Product Development", min_value = 0, max_value=100, value =defmicrobiome)
livingtherapy = st.sidebar.slider(label = "Living Therapy Product Development", min_value = 0, max_value=100, value =deflivingtherapy)


st.sidebar.caption("Define a risk associated with the size of the company. This should be a number between 0 and 1 which represents the risk associated with a smaller company. In other words, for two companies requesting the same project what do we estimate is the biggest increase in overall risk % associated with that smaller size due to resource constraints, default risk, lack of track record, etc. By defualt, I'll estimate that its 20% more risky to take on a smaller company as a partner compared to a larger company, so in that case I would set this to be 0.2.")
sizerisk_coeff  = st.sidebar.slider(label = "Size Risk Coefficient", min_value = 0, max_value=1, value =defsizerisk_coeff, step=0.01)


st.sidebar.caption("let's assume that https://www.failory.com/blog/startup-failure-rate 60% of startups fail within the first five years if that is the case, then we can use that as the base case for whether the startup will fail or not and reduce from there based on 1. the fact that Ginkgo is lending this startup its resources, and 2. that Ginkgo has vetted this team's leadership and product potential itself with that in mind, define a coefficient to multiply this 45% by that will represent the risk reduction relative to a general startup caused by the association with Ginkgo")
startup_risk_coeff  = st.sidebar.slider(label = "Startup Risk Coefficient", min_value = 0.0, max_value=1.0, value =defstartup_risk_coeff, step=0.01)

st.sidebar.caption("we have already decided a difficulty risk associated with each organism, but we should also add an input to determine how much weight the user would like to simulate organism difficulty as part of the simulation. We default to 1")
organism_difficulty_scalar  = st.sidebar.slider(label = "Organism Difficulty Scalar", min_value = 0.0, max_value=10.0, value =deforganism_difficulty_scalar, step=0.01)


st.sidebar.caption("if the customer is a returning customer, we would like to know, because that will change the risks associated. We want to define a probability that the customer is a returning customer, and we will default that to 30%")
returning_customer_prob  = st.sidebar.slider(label = "Returning Customer Probability", min_value = 0.0, max_value=1.0, value =defreturning_customer_prob, step=0.01)

st.sidebar.caption("also indicate the associated reduction of total risk with returning customers")
returning_customer_risk_reduction_coeff  = st.sidebar.slider(label = "Returning Customer Probability", min_value = 0.0, max_value=1.0, value =defreturning_customer_risk_reduction_coeff, step=0.01)



industry_breakdown = [consumertech, induenv, ag, foodag, pharma, defense]
size_breakdown = [under20, under100, under1000, under100000]
type_risk_breakdown = [proteinexp, hetbiosynth, celllineopt, microbiome, livingtherapy]


simulate = st.sidebar.button("SIMULATE")

if simulate:
    ginkgo_customer_generator(1, industry_breakdown, size_breakdown, sizerisk_coeff, startup_risk_coeff, type_risk_breakdown, organism_difficulty_scalar,returning_customer_prob, returning_customer_risk_reduction_coeff)
