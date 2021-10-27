from os import write
import random
import time
import streamlit as st
import math


ark_logo_string = r'<svg viewBox="113.514 153.677 336.623 162.626" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">  <image width="338" height="164" x="114.525" y="154.311" xlink:href="data:image/png;base64,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"/></svg>'
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
        prefixes = ["myo","ophthalmo","partheno","branchio","countero","erythro","proprio","saccharo","thrombo","tropic","arterio","astero","blasto","brachio","brachyo","broncho","carcino","novo","carpalo","cephalo","cerebro","cervico","chondro","contrao","dactylo","oectomy","ognatho","ognosis","hectoro","hetero","hystero","ichthyo","lachryo","myriado","neprho","ornitho","permeao","ophobia","physico","pneumo","pseudo","psycho","stereo","tracheo","oalgia","andro","anemo","antero","antho","arthro","bradyo","caloro","capito","cardio","centio","centro","chloro","chrono","cotylo","cranio","crypto","ocycle","dendro","digito","diplo","dynamo","entomo","extrao","ferro","fracto","glosso","glyco","gymno","hypero","oiasis","infrao","intero","intrao","karyo","kerato","linguo","lumeno","malaco","malleo","micro","millio","morpho","multio","mycelo","necro","nemato","neuro","odonto","oligo","proto","pachyo","paleo","phago","photo","phreno","phyco","pinnio","platyo","pleuro","pulmo","quadro","retro","rhino","rhodo","sclero","script","stello","tachyo","tarso","thallo","thermo","transo","tricho","tropho","ultrao","ventro","xantho","adeno","adipo","aero","agrio","alto","ambio","amebo","amnio","amylo","angio","anteo","antio","atmo","audio","auto","baro","carno","carpo","catao","caudo","chemo","chiro","collo","conio","corpo","cutio","cyano","decao","decio","demio","dento","dermo","dormo","dorso","ecto","equio","euryo","floro","folio","foreo","gluto","graph","gravo","halo","hemio","herbo","herpo","hidro","histo","holo","homo","homo","horto","hydro","hygro","soma","modal","exacto","ninjet","hypho","hypo","kilo","lacto","ligno","mammo","margo","masto","meso","meter","metho","mito","moleo","mono","morto","myco","oculo","omnio","onco","ortho","oscuo","palmo","pento","perio","phylo","pino","polyo","porto","posto","propo","ptero","quino","radio","rhizo","roto","rupto","sapro","sarco","semio","septo","sesso","somno","steno","stylo","telo","terro","turbo","vecto","volv","ovor","xer","alb","ana","ang","aqua","oase","aur","avi","sider","diao","diso","dys","eco","epi","eth","gam","gen","gyro","ign","iso","kel","lato","lipo","loco","luna","malo","medo","mego","meso","mido","mino","miso","myco","naso","neo","nova","nuco","octo","olfo","oleo","onco","opto","orbo","oto","oxyo","pano"]
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
        suffixes = ["gene","cyte","Dx","sion","bio","omics","ros","Maker","ome","amo","Shift","Fuse","Cure","lytics","lictics","listics","Ion","fication","Bounty","Saur","exis","Thrive","Life","Finity","vero","ntech","Gate","trex","Logic","Gem","genic","Venn","ware","cessory","oxa","bolomics","exa","vexa","tify","ctify","Forge","Max","Prime","vio","vax","vantia","thority","licity","lix","ovi","mat","core","nol","xon","biotic"]

        random_name = random.choice(prefixes) + random.choice(suffixes)
        random_name = random_name.replace("oo","o")
        random_name = random_name.replace("aa","a")
        random_name = random_name.replace("yy","y")
        random_name = random_name.replace("uu","u")
        random_name = random_name.replace("ii","i")


        return random_name
    else:
        lastnames = ["Adams","Adams","Murphy","Murphy","Phillips","Phillips","Martin","Martin","Anderson","Anderson","Lee","Lee","Jackson","Jackson","Bell","Bell","Myers","Myers","White","White","Stewart","Stewart","Clark","Clark","Harris","Harris","Perry","Perry","Bailey","Bailey","Watson","Watson","Nelson","Nelson","King","King","Sanders","Sanders","Young","Young","Butler","Butler","Walker","Walker","Davis","Davis","Roberts","Roberts","Green","Green","Hall","Hall","Carter","Carter","Miller","Miller","Morris","Morris","Cox","Cox","Parker","Parker","Reed","Reed","Cooper","Cooper","Rogers","Rogers","Collins","Collins","Moore","Moore","Wood","Wood","Richardson","Richardson","Barnes","Barnes","Smith","Smith","Powell","Powell","Peterson","Peterson","Wilson","Wilson","Lewis","Lewis","Morgan","Morgan","Robinson","Robinson","Turner","Turner","Campbell","Campbell","Hughes","Hughes","Ward","Ward","Cook","Cook","Mitchell","Mitchell","Taylor","Taylor","Wright","Wright","Johnson","Johnson","Bennett","Bennett","Allen","Allen","Jones","Jones","Brooks","Brooks","Fisher","Fisher","Brown","Brown","Thomas","Thomas","Hill","Hill","Price","Price","Scott","Scott","Edwards","Edwards","Ross","Ross","Gray","Gray","Kelly","Kelly","Russell","Russell","Sullivan","Sullivan","Evans","Evans","Baker","Baker","Thompson","Thompson","Jenkins","Jenkins","Williams","Williams","Howard","Howard","Foster","Foster","James","James","Sheridan","Sheridan","Abbott","Abbott","Nicholls","Nicholls","Curtis","Curtis","Nicholas","Nicholas","Thomson","Thomson","Brooke","Brooke","Emery","Emery","Berry","Berry","Bob","Bob","Millard","Millard","Bond","Bond","Fuller","Fuller","Jarvis","Jarvis","Samuel","Samuel","Flynn","Flynn","Boyd","Boyd","Black","Black","Forrest","Forrest","Wade","Wade","Charlton","Charlton"]
        lastname1 = random.choice(lastnames)
        lastname2 = random.choice(lastnames)
        colors = ["red","green","blue","yellow","cyan", "magenta"]
        random_name = (lastname1 + " & " + lastname2)
        return random_name

def generate_description(name, industry):
    #pharma
    colors = ["red","green","blue","yellow","cyan", "magenta"]
    if industry == "Biopharma":
        diseases = ["Acromegaly","Addison disease","Adult respiratory distress syndrome (ARDS)","AIDS","ALS (Amyotrophic lateral sclerosis)","Amyloidosis","Anemia","Iron deficiency","B12 and folate deficiency","Thalassemia","Sickle Cell","Spherocytosis","Aneurysms","Ankylosing spondylitis (HLA B27)","Arteritis","Polyarteritis nodosa","Arthritis","Asthma","Atherosclerosis","Autoimmune disease","Systemic Lupus Erythmetosus","Sjögren syndrome","Dermatomyositis","Scleroderma","Bleeding disorders","Hemophilia","von Willebrand disease","Thrombocytopenia","Henoch-Schοnlein purpura","Brain edema and herniation","Breast diseases","Fibrocystic change","Fibroadenoma","Mastitis","Bronchiectasis","Calcium-phosphate homeostasis","Cardiomyopathy","Celiac disease","Cholecystitis/lithiasis","Cirrhosis","Congenital heart disease","COPD","Emphysema","Chronic bronchitis","Pneumoconioses","Bronchiolitis obliterans (BOOP)","Coronary Heart Disease","Angina","Creutzfeldt-Jakob disease","Crohn disease","Cushing syndrome","Cystic fibrosis","Dementia","Alzheimer's Diseease","Dermatitis","Dermatomycoses","Diabetes insipidus","Diabetes mellitus","Diarrhea","Disseminated intravascular coagulation","Diverticular disease of G.I. tract","Dyslipoproteinemia","Familial hypercholesterolemia","Dysphagia","Achalasia","Barrett esophagus","Eczema","Encephalitis","Endocarditis","Libbman-Sacks","Enterocolitis","Epilepsy","Erythema multiforme","Esophagitis","Fungal infection","Candidiasis","Aspergillosis","Histoplasmosis","Cryptococcosis","Coccidioidomycosis","Glaucoma","Glomerulonephritis","Gout","Graves disease","Growth abnormalities","Dwarfism","Gigantism","Guillain-Barre Syndrome","Hemochromatosis","Hepatitis","Hodgkin disease","Hydrocephalus","Hypertension","Hypogonadism","Turner syndrome","Klinefelter syndrome","Immune diseases of liver","Autoimmune hepatitis","Infectious mononucleosis","Infertility","Intracranial hemorrhage","Kidney diseases","Leukemia","Lyme disease","Lymphoma","Malabsorption syndromes","Malaria","Meningitis","Multiple myeloma","Multiple sclerosis","Muscular dystrophy","Myasthenia gravis","Myeloproliferative disorders","Myocarditis","Myositis","Dermatomyositis","Polymyositis","Infectious myositis","Nephropathy, peripheral","Obstructive","Interstitial","Amyloid related","Infectious","Neuroblastoma","Neuropathy","Obesity","Osteoarthritis","Otitis media","Ovarian dysfunction","Cysts","Premature ovarian failure","Paget disease of bone","Pancreatitis","Parkinson disease","Pericarditis","Pericardial tamponade","Pharyngitis","Pheochromocytoma","Platelet disorders","Thrombocytopenia","Thrombasthenia","Polycystic kidney disease","Potassium homeostasis disorders","Psoriasis","Pyelonephritis","Renal failure","Retinal diseases","Retinoblastoma","Rheumatic fever","Rheumatoid arthritis","Sarcoidosis","Sepsis","Sexually transmitted diseases","Sodium homeostasis diseases","Spinal cord disease","Trauma","Demyelinating diseases","Polyomyelitis","Spongiform encephalopathies","Syphilis","Systemic lupus erythematosus","Systemic sclerosis (scleroderma)","Thrombosis","Embolism","Hypo/hyper function","Thyroiditis","Toxic shock syndrome","Tranfusion complications","Transplantation","Tuberculosis"]
        terms0 = ["radiolabeled ","florophore-tagged ", "chromophore-tagged ", "ultracompact ","L-enantiomeric ","R-enantiomeric ","novel mode-of-action ","clinically-tested ","immunogenic ","tumor-infiltrating "]
        terms1 = ["antisense oligos", "vaccine adjuvants","aptamers","vaccines","gene-therapies","lipid nanoparticles","virus-like particles","monoclonal antibodies", "protein kinase inhibitors", "naturally occuring immunosuppressive molecules", "viral coat proteins","antimicrobial peptides","small molecule therapeutics"]
        description = name + " is a company known for manufacturing " + (random.choice(terms0)+ random.choice(terms1)) + " for the treatment of " + random.choice(diseases).lower() + ". However, they would like to begin manufacturing these therapeutics on a cellular platform."

    #indu/env

    if industry == "Industrial/Environmental":
        terms1 = ["phytoremediation", "radioactive waste management", "food wastage", "environmental cleanup", "direct-air carbon capture", "climate change","water purification", "honeybee endangerment","desalination","ocean pollution"]
        terms2 = ["government subsidized research", "yogurt-based neuromorphic computing","hyperparameter optimization","bioengineering", "biomechatronics", "NFTs", "ESG-conscious corporate architecture", "biosensors", "first principles engineering", "biohacking","in silico biology", "artificial intelligence", "blockchain", "drone imaging", "ai-enabled analytics", "protein-protein interaction predictions", "molecular modelling"]
        terms3 = ["tackle", "solve","monetize","revolutionize indstry-wide approaches to","understand"]
        terms5 = ["unique","novel","ancient","magical","innovative","unusual","orthogonal","top-down","bottom-up"]
        terms4 = ["age-old", "pervasive", "terrible","persistent","serious","decades-old","previously thought-to-be impossible", "enormous"]
        description = name + " is an environmental/ESG-focused company that is trying to " +random.choice(terms3)+" the " + random.choice(terms4) + " problem of " + random.choice(terms1) + " using a " +random.choice(terms5) + " approach to " + random.choice(terms2)+". They would like Ginkgo to help them develop their new product using cell engineering."
    #agbio
    if industry == "Agricultural Biology":
        regions = ["rhizosphere-associating","phytosphere-associating","plant holobiome-associating", "soil-bourne", "seed coatings of", "in furrow suspension sprays of"]
        microbetypes = ["viruses", "viroids","bacteria","protozoa","fungi","oomycetes","microbial consortia"]
        plant_types = ["rice","corn","sorghum","wheat","soybeans", "alfalfa","cassava","potatoes", "grapes","cotton","onions","garlic","bananas","oilseed rape","barley"]
        enhance_protect = ["enhance plant growth", "enhance plant immunity","boost photosynthetic output","fix atmospheric nitrogen", "solubilize inorganic phosphorous", "generate bioavailable potassium","chelate soil iron sources","accumulate soilbourne heavy metals"]

        description = name + " is an AgBio company focused on developing " + random.choice(regions) + " " +random.choice(microbetypes) + " that can " + random.choice(enhance_protect) + " in " + random.choice(plant_types) + ". They would like Ginkgo to help with that."
    #consumertech
    if industry == "Consumer Technology":
        adjectives = ["incredible", "low-cost", "bespoke","artisanal", "hand-crafted", "heirloom","authentic","best-in-class","world-renown"]
        sizzler = ["non-fungible","organic", "non-gmo", "genetically engineered","ethically-sourced", "plant-based","locally grown", "gluten-free","lactose-free","hypoallergenic", "all-natural"]
        products = ["smart watches","deodorant","toothpaste","tuxedos","sour candy","soap","tampons","eye-liner","facial tissue","moisturizer","lip balm","lotion","razor blades","cologne","shoe polish","sunscreen","hair gel","mirrors","mouthwash","dental floss","sun glasses","mobile phones", "perfume", "eyeshadow", "lipstick", "shampoo", "hairspray", "eye drops", "yoga mats", "microscope filters","optical coatings","personal lubricants"]
        description = name + " is a consumer tech company that is known for their "+ random.choice(adjectives) + " " + random.choice(sizzler) + " " + random.choice(products) + ". They would like Ginkgo to help them develop cell lines for a new product suite."


    #food
    if industry == "Food/Beverage":
        sizzler = ["organic", "non-gmo", "ethically-sourced", "locally grown", "gluten-free","farm-to-market","animal welfare-approved","fair trade", "grass fed","hormone-free","antibiotic-free","all-natural", "free range","lactose-free","hypoallergenic", "all-natural"]
        products = ["hamburgers", "crepes", "breast milk", "cakes", "gelato", "corn flakes","pizza","hot dogs","shellfish","parmesan","waffles","espresso","instant coffee","marshmallows","mayonnaise","soft drinks", "curry paste","tortillas","sourdough","soylent","meatballs", "chibben tendies","chibben tendies","chibben tendies","chibben tendies","beer", "kombucha","french fries", "meal replacement shakes","cookies"]
        description = name + " is a food and beverage company that is trying to develop microbially-produced " + random.choice(sizzler) + " " + random.choice(products)+". They are hoping Ginkgo will help them figure out some issues they're having."
        pass
    #defense
    if industry == "Defense":
        sizzler = ["nuclear powered","solar powered","thermally resistant", "adaptive, armor plated", "bullet-proof", "nanobot-containing", "advanced", "ballistic", "subsonic", "stealth", "hypersonic", "suborbital", "geostationary"]
        products = ["film coatings", "bullets", "explosives", "fuel", "body armor","battle tanks", "scout vehicles", "combat stimulant autoinjectors", "humanioid attack robots","nuclear weapons","sniper rifles", "precision lasers", "stealth field generators","fragmentation grenades", "napalm", "UAVs","missiles","attack drones", "satellites","pepper spray","area denial devices","land mines","torpedoes","biological agents","mortar shells","smoke cannisters","pyrotechnic devices","aircraft missile protection systems","electronic warfare modules","electronic counter measures","depth charges","plasticizers","additive coupling agents","high velocity kinetic weapon ammunition","particle beam emmitters","flame throwers","gas mask cannisters","ballistic protection panels", "radar warning systems", "electronic counter countermeasures","range-gate pull off emitters","signal jamming equipment","Troposcatter-radio communication equipment","non-metallic protective garments"]
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
    ecoli["diffrisk"] = (((3+3+3+3+(10*(500/2000)))/5)*10)

    yeast = {}
    yeast["name"] = "yeast"
    yeast["domain"] = "eukaryote"
    yeast["doubling time"] = 90
    yeast["sterility reqs"] = difficulties[1]
    yeast["td"] = difficulties[1]
    yeast["genome size"] = 12
    yeast["gapf"] = difficulties[0]
    yeast["hd"] = difficulties[0]
    yeast["diffrisk"] = (((3+3+6+6+(10*(500/2000)))/5)*10)


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
        species_names = ["aurantis","pierius","simonius","aliius","streptococci","israelii","tumefaciens","coli","radiobacter","anthracis","thuringiensis","subtilis","botulinum","difficile","cepacia","faecium","carotovora"]
        
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
        random_bacterium["diffrisk"] = (((3*dr1)+(3*dr2)+(3*dr3)+3+(10*(500/2000)))/5)*10
        organism_choice = random_bacterium
    elif organism_type == "Alternative Fungus":
        letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        species_names = ["niger","flavus","augustus","sinensis","cornea","nidulans","rubicundus","birnbaumii","molybites","emodensis","cubensis","azurecens","solani","omnivora","grandis","thermophila","versicolor","bisporus","erinaceous"]
        
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
        random_fungus["diffrisk"] = (((3*dr1)+(3*dr2)+(3*dr3)+(3*dr4)+(10*(500/2000)))/5)*10
        organism_choice = random_fungus
    else:
        st.write("couldnt find organism")
    

    project_type_int = random.randint(0,(len(project_types)-1))
    project_type = project_types[project_type_int]
    project_type_risk = project_type_risks[project_type_int]



    project = [organism_choice, project_type, project_type_risk]
    return project

def ginkgo_customer_generator(number_to_generate, industry_breakdown, size_breakdown, sizerisk_coeff, startup_risk_coeff,type_breakdown,organism_difficulty_scalar,returning_customer_prob, returning_customer_risk_reduction_coeff,failure_risk_modulus, verbose):

    intellectual_property_points_accumulated = 0
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

        project = generate_project(industry,size,type_breakdown) #generate the project
        organism = project[0]
        specs = project[1]
        project_risk = project[2]
        

        #simulate the customer
        st.write("\n\n-----------------------BEGIN CUSTOMER SIMULATION--------------------")
        st.write(name + " is a company in the " + industry + " industry with a $" + "{:,}".format(size) + " market capitalization.\n")

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
        adjusted_organism_difficulty_risk = (1-(1-organism["diffrisk"] * organism_difficulty_scalar))/100
        st.write("This company wants Ginkgo to use the organism " + organism["name"] + " for this project. " + organism["name"].capitalize() + " is a " + organism["domain"] + " with a doubling time of " + str(organism["doubling time"])+" minutes.\n")
        st.write(organism["name"].capitalize()+ " is an organism which has a " + organism["td"] + " transformation difficulty, has sterility requirements that make working with it in the lab " + organism["sterility reqs"] + ", has a genome annotation that makes working with it " + organism["gapf"]+", and because of how robust/weak it is in the face of shearing forces, handling it in the lab is " + organism["hd"]+".\n")
        st.write(organism["name"].capitalize() + ' has an associated ' + str(round(adjusted_organism_difficulty_risk*100,2)) + r'% organism difficulty risk, where 100% is the highest risk rating and 0% is the lowest risk rating.' +"\n")
        st.write("The project is your basic " + specs.lower() + " type of thing. These kinds of projects have an associated " + str(round(project_risk*100,2)) + '%' + " failure risk. \n")   

        overall_risk_num = (((project_risk + adjusted_organism_difficulty_risk)/2)*returning_customer_risk_coefficient*size_risk*industry_risk)*100

        # st.write("project risk: " + str(project_risk))
        # st.write("adj_organism diff risk: " + str(adjusted_organism_difficulty_risk))
        # st.write("returning_customer_risk_coefficient: " + str(returning_customer_risk_coefficient))
        # st.write("size risk: " + str(size_risk))
        # st.write("industry risk: " + str(industry_risk))


        risk_display_num = overall_risk_num/100
        overall_risk_percent = round(risk_display_num*100,2)
                
        overall_risk = str((round(risk_display_num*100,2)))+"%"
        st.write("This project has approximately a " + overall_risk + " per-iteration failure risk.\n")

        simready = "y"
        # simready = input("Ready to simulate? (y/n):\n>")
        if simready.lower() == "y":
            st.write("Simulating project with " + name +", attempting to do " + project[1] + " in " + organism["name"])
            y1successful = False
            y2successful = False
            years = 1
            totalfailurecount = 0
            failurecount = 0
            while y1successful == False:
                if failurecount > 10:
                    failurecount = 9
                randomrating = (random.randint(totalfailurecount*2,1000)/10) * (1-(failurecount/failure_risk_modulus))
                if verbose == True:
                    st.write("simulating phase 1 iteration, roll was " + str(round(randomrating,0)) + " -- trying to beat " + str(round(overall_risk_num,0)))
                if randomrating > overall_risk_num:
                    years = years + .5
                    st.write("Project year 1 successful. Project time elapsed = " +str(years*12) + " months...")
                    failurecount = 0
                    y1successful = True
                else:
                    years = years+.5
                    failurecount+=1
                    totalfailurecount +=1
                    if verbose == True:
                        st.write("Setback occured. Project time elapsed = " +str(years*12) + " months...")
                if totalfailurecount > 20:
                    break
            
            while y2successful == False:
                if totalfailurecount > 20:
                    break
                if failurecount > 10:
                    failurecount = 9
                randomrating = (random.randint(totalfailurecount*2,1000)/10) * (1-(failurecount/failure_risk_modulus))
                if verbose == True:
                    st.write("simulating phase 2 iteration, roll was " + str(round(randomrating,0)) + " -- trying to beat " + str(round(overall_risk_num,0)))

                if randomrating > overall_risk_num:
                    years = years + .5
                    st.write("Project year 2 objectives successful. Project time elapsed = " +str(years*12) + " months...")
                    y2successful = True
                else:
                    years = years+.5
                    failurecount +=1
                    totalfailurecount +=1
                    if verbose == True:
                        st.write("Setback occured. Project time elapsed = " +str(years*12) + " months...")
                if totalfailurecount > 20:
                    projectfailure = True
                    break
                    
            if y1successful:
                if y2successful:
                    projectfailure = False
                    st.write("Project successfully completed in " + str(years*12) + " months.")
                else:
                    projectfailure = True
            else:
                projectfailure = True

            if projectfailure == True:
                st.write("This project completely failed resulting in " + str(years*12) + " months of wasted time")
                intellectual_property_points_accumulated = intellectual_property_points_accumulated + overall_risk_percent/4
            else:
                st.write("Ginkgo delivered on their milestones and customer specifications!")
                intellectual_property_points_accumulated = intellectual_property_points_accumulated + overall_risk_percent
            
                #if it is a midcap company, we'll say there is a 50% chance that Ginkgo negotiated an equity agreement and 50% chance they negotiated cash
                cashonly = False
                if size < 200000000:
                    if size > 20000000:
                        cashchanceint = random.randint(1,100)
                        if cashchanceint > 25:
                            cashonly = True
                #if it is a largecap company, we'll say there is a 50% chance that Ginkgo negotiated an equity agreement and 50% chance they negotiated cash
                elif size > 200000000:
                    cashonly = True
                else:
                #if it is a micro/small cap company, its a 0% chance that the negotiated revenue is cash.
                    cashonly = False
            
                #if the payment was negotiated to be cash, then we can estimate it was a payment worth 10,000,000-15,000,000 for a mid cap company, 20,000,000 for a large cap company
                cash_payment = 0
                if cashonly == True:
                    if size < 100000000:
                        cash_payment = (((random.randint(1,100)/100 * 5000000) + 10000000))
                        if cash_payment > (0.15*size):
                            cash_payment = 0.2 *size
                        if cash_payment < 5000000:
                            cash_payment = 5000000
                    if size > 100000000:
                        cash_payment = (random.randint(1,100)/100 * 5000000) + 20000000
                        if cash_payment > (0.15*size):
                            cash_payment = (0.2*size)
                        if cash_payment < 10000000:
                            cash_payment = 10000000
                    else:
                        cash_payment = 0.1*size
                        if cash_payment < 10000000:
                            cash_payment = 10000000 + (10000000*(random.randint(50,100)/100))
                    total_cash_payments = total_cash_payments + (cash_payment)
                    st.write(name + " compensated Ginkgo with a cash payment of $" + str("{:,}".format(round(cash_payment,0))))
                
                if cashonly == False:
                    #first check to see if this company just straight up fails
                    startup_survival_probability = (1-(startup_survival_probability*100))
                    startuprandint = random.randint(1,100)
                    if startup_survival_probability < startuprandint:
                        st.write("This company rolled high enough to not fail as a startup!")
                        cagr_negative = False
                    else:
                        st.write("Unfortunately, this startup will fail before it's 6th year of existence.")
                        cagr_negative = True
                    if cagr_negative == False:
                        cagr = random.randint(0,50)/100
                    else:
                        cagr = random.randint(-5,-25)/100 

                    
                    equity_comp = size*.15
                    st.write("This company has compensated Ginkgo for its services with $" + str("{:,}".format((round(size*.15,2)))) + " worth of its equity, which has a " + str(round((cagr*100),2)) + r"% CAGR")
                    total_equity_compensations.append((equity_comp,cagr))

            st.write("-----------------------SIMULATION COMPLETE-------------------")
            st.write("Total intellectual property points accumulated: " + str(round(intellectual_property_points_accumulated,2)))
            st.write("Total cash accumulated $" + str("{:,}".format(round(total_cash_payments,2))))
            # customer_data = []
            # customer_data.append(name)
            # customer_data.append(industry)
            # customer_data.append("{:,}".format(size))
            # if projectfailure == True:
            #     customer_data.append("FAIL")
            # else:
            #     customer_data.append("SUCCESS")
            # customer_data.append(str(years*12))
            # customer_data.append(project[1])
            # customer_data.append(organism["name"])
            # customer_data.append(str(organism["diffrisk"])+"%")
            # customer_data.append(overall_risk)
            counter+=1
    #         customer_results.append(customer_data)
    
    # st.write("This customer " + str(1) + " has resulted in a total of $" + str("{:,}".format(total_cash_payments))+" cash payments to Ginkgo.")
    
    # if len(total_equity_compensations) > 0:
    #     equity = 0
    #     wcagrsum = 0
    #     for equitypayment in total_equity_compensations:
    #         equity = equity + equitypayment[0]
    #         wcagrsum = wcagrsum + (equitypayment[0] * equitypayment[1])

    #     wcagrav = wcagrsum /len(total_equity_compensations)
    #     wcagr = wcagrav/equity
    #     st.write("This customer has awarded Ginkgo $" + str("{:,}".format(round(equity,2))) + " of equity which has a " +str((round(wcagr*100,2))) + "% CAGR.")


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

deforganism_difficulty_scalar = 1.0

#if the customer is a returning customer, we would like to know, because that will change the risks associated.
#we want to define a probability that the customer is a returning customer, and we will default that to 30%

defreturning_customer_prob = .3

#and the associated reduction of total risk with returning customers should also be an input

defreturning_customer_risk_reduction_coeff = .66

#we also define a failure risk modulus which is a number between 1 and 20 that represents how likely it is that failed project iterations lead to more failed project iterations.
#the higher this number is, the less likely it is that failed iterations indicate that the project is probably going to fail overall

deffailure_risk_modulus = 3

st.title("Ginkgo Customer Generator v0.1")

st.sidebar.image(ark_logo_string, use_column_width='always', width = 10)

st.sidebar.caption("Disclosure: This is a toy that randomly generates fictional companies that might be customers for Ginkgo Bioworks. The companies are not real, and the output is not indicative of ARK's estimation of Ginkgo's actual capabilities or success rates. This is meant for entertainment purposes only.")


simulate = st.sidebar.button("SIMULATE")
st.sidebar.caption("Press this button to simulate a random Ginkgo customer project using the inputs below.")


defverbosity = False
verbose = st.sidebar.checkbox("Verbose?", value = defverbosity, help = "Check this box if you would like to display simulation rolls and more verbose output.")


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

st.sidebar.caption("Define a risk associated with the size of the company. This should be a number between 0 and 1 which represents the risk associated with a smaller company. In other words, for two companies requesting the same project what do we estimate is the biggest increase in overall risk % associated with that smaller size due to resource constraints, default risk, lack of track record, etc. By defualt, I'll estimate that its 20% more risky to take on a smaller company as a partner compared to a larger company, so in that case I would set this to be 0.2.")
sizerisk_coeff  = st.sidebar.slider(label = "Size Risk Coefficient", min_value = 0.01, max_value=1.0, value =defsizerisk_coeff, step=0.01)


st.sidebar.caption("let's assume that https://www.failory.com/blog/startup-failure-rate 60% of startups fail within the first five years if that is the case, then we can use that as the base case for whether the startup will fail or not and reduce from there based on 1. the fact that Ginkgo is lending this startup its resources, and 2. that Ginkgo has vetted this team's leadership and product potential itself with that in mind, define a coefficient to multiply this base startup failure rate by. This will therefore represent the risk reduction relative to a general startup caused by the association with Ginkgo")
startup_risk_coeff  = st.sidebar.slider(label = "Startup Risk Coefficient", min_value = 0.01, max_value=1.0, value =defstartup_risk_coeff, step=0.01)

st.sidebar.caption("we have already decided a difficulty risk associated with each organism, but we should also add an input to determine how much weight the user would like to simulate organism difficulty as part of the simulation. We default to 1")
organism_difficulty_scalar  = st.sidebar.slider(label = "Organism Difficulty Scalar", min_value = 0.01, max_value=10.0, value =deforganism_difficulty_scalar, step=0.01)


st.sidebar.caption("if the customer is a returning customer, we would like to know, because that will change the risks associated. We want to define a probability that the customer is a returning customer, and we will default that to 30%")
returning_customer_prob  = st.sidebar.slider(label = "Returning Customer Probability", min_value = 0.01, max_value=1.0, value =defreturning_customer_prob, step=0.01)

st.sidebar.caption("also indicate the associated reduction of total risk with returning customers")
returning_customer_risk_reduction_coeff  = st.sidebar.slider(label = "Returning Customer Risk Reduction Coefficient", min_value = 0.01, max_value=1.0, value =defreturning_customer_risk_reduction_coeff, step=0.01)

st.sidebar.caption("we also define a failure risk modulus which is a number between 1 and 20 that represents how likely it is that failed project iterations lead to more failed project iterations. The higher this number is, the less likely it is that failed iterations indicate that the project is probably going to fail overall")
failure_risk_modulus  = st.sidebar.slider(label = "Failure Risk Modulus", min_value = 1, max_value=20, value =deffailure_risk_modulus)

defnumbergen = 1
st.sidebar.caption("specify how many companies you would like to simulate in this run")
numbergen  = st.sidebar.slider(label = "Customers to generate", min_value = 1, max_value=1000, value =defnumbergen)


industry_breakdown = [consumertech, induenv, ag, foodag, pharma, defense]
size_breakdown = [under20, under100, under1000, under100000]
type_risk_breakdown = [defproteinexp/100, defhetbiosynth/100, defcelllineopt/100, defmicrobiome/100, deflivingtherapy/100]



if simulate:
    ginkgo_customer_generator(numbergen, industry_breakdown, size_breakdown, sizerisk_coeff, startup_risk_coeff, type_risk_breakdown, organism_difficulty_scalar,returning_customer_prob, returning_customer_risk_reduction_coeff,failure_risk_modulus, verbose)
