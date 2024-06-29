import json

import streamlit as st
import numpy as np
import pandas as pd
import tensorflow as tf
import keras.preprocessing.image as ImageDataGenerator
from PIL import Image


import streamlit as st 
from streamlit_lottie import st_lottie 

#For Lootie Aimation
def load_lottiefile(filepath: str):
    with open(filepath,"r") as f:
        return json.load(f)
# Return Index
def model_prediction(test_image):
    # Load .h5 model 
     model = tf.keras.models.load_model('plant_model.h5')
     image = tf.keras.preprocessing.image.load_img(test_image,target_size=(128,128))
     input_arr = tf.keras.preprocessing.image.img_to_array(image)
     input_arr = np.array([input_arr])
     prediction = model.predict(input_arr)
     # Example prediction result (replace with your actual prediction result)
     result = np.argmax(prediction) ## Here Index Is Coming
     return result    
# Return Disease Name
def diseases(result: int):
    # Array Of Diseaseas
    class_names = [
    'Apple Scab',
    'Apple Black Rot',
    'Cedar Apple Rust',
    'Apple Healthy',
    'Blueberry Healthy',
    'Cherry Powdery Mildew',
    'Cherry Healthy',
    'Corn Cercospora Leaf Spot Gray Leaf Spot',
    'Corn Common Rust ',
    'Corn Northern Leaf Blight',
    'Corn Healthy',
    'Grape Black Rot',
    'Grape Esca (Black Measles)',
    'Grape Leaf Blight (Isariopsis Leaf Spot)',
    'Grape Healthy',
    'Orange Haunglongbing (Citrus Greening)',
    'Peach Bacterial Spot',
    'Peach Healthy',
    'Pepper, Bell Bacterial Spot',
    'Pepper, Bell Healthy',
    'Potato Early Blight',
    'Potato Late Blight',
    'Potato Healthy',
    'Raspberry Healthy',
    'Soybean Healthy',
    'Squash Powdery Mildew',
    'Strawberry Leaf Scorch',
    'Strawberry Healthy',
    'Tomato Bacterial Spot',
    'Tomato Early Blight',
    'Tomato Late Blight',
    'Tomato Leaf Mold',
    'Tomato Septoria Leaf Spot',
    'Tomato Spider Mites Two-Spotted Spider Mite',
    'Tomato Target Spot',
    'Tomato Yellow Leaf Curl Virus',
    'Tomato Mosaic Virus',
    'Tomato Healthy'
]
    return class_names[result]
# Return Cure
def cure(result: int):
    plant_disease_cures = [
    [
        "1. Use fungicides such as captan or myclobutanil.",
        "2. Remove and destroy infected leaves and fruit.",
        "3. Prune trees to improve air circulation.",
        "4. Avoid overhead irrigation to reduce leaf wetness.",
        "5. Apply dormant oil to control overwintering fungal spores."
    ],
    [
        "1. Prune trees for better air circulation.",
        "2. Remove and destroy infected fruit and leaves.",
        "3. Apply fungicides like myclobutanil or pyraclostrobin.",
        "4. Use copper sprays during the growing season.",
        "5. Maintain good orchard hygiene to reduce overwintering spores."
    ],
    [
        "1. Remove cedar trees near apple orchards if possible.",
        "2. Apply fungicides like triadimefon or myclobutanil.",
        "3. Prune apple trees to improve air circulation.",
        "4. Apply sulfur sprays during the growing season.",
        "5. Remove and destroy any infected leaves or fruit."
    ],
    [
        "No specific treatment needed; maintain good orchard practices."
    ],
    [
        "No specific treatment needed; maintain good cultural practices."
    ],
    [
        "1. Apply fungicides like sulfur or potassium bicarbonate.",
        "2. Prune trees to improve air circulation.",
        "3. Remove and destroy infected leaves and shoots.",
        "4. Apply neem oil to suppress fungal growth.",
        "5. Avoid overhead irrigation to reduce leaf wetness."
    ],
    [
        "No specific treatment needed; maintain good orchard practices."
    ],
    [
        "1. Use fungicides like chlorothalonil or mancozeb.",
        "2. Rotate crops to reduce disease carryover.",
        "3. Plant resistant varieties if available.",
        "4. Remove and destroy infected leaves and debris.",
        "5. Apply copper-based sprays during humid conditions."
    ],
    [
        "1. Plant resistant corn varieties if available.",
        "2. Apply fungicides like triazole or strobilurin.",
        "3. Rotate crops and practice good field hygiene.",
        "4. Remove and destroy infected crop residues.",
        "5. Ensure proper plant spacing for better air circulation."
    ],
    [
        "1. Apply fungicides like azoxystrobin or pyraclostrobin.",
        "2. Rotate crops to break disease cycles.",
        "3. Use resistant corn hybrids if available.",
        "4. Remove and destroy infected leaves and debris.",
        "5. Avoid excessive nitrogen fertilization."
    ],
    [
        "No specific treatment needed; maintain good agricultural practices."
    ],
    [
        "1. Apply fungicides like captan or myclobutanil.",
        "2. Remove and destroy infected fruit clusters.",
        "3. Prune vines to improve air circulation.",
        "4. Apply dormant oil to reduce overwintering spores.",
        "5. Practice good vineyard sanitation."
    ],
    [
        "1. Remove and destroy infected grapevine wood.",
        "2. Apply systemic fungicides like fosetyl-aluminum.",
        "3. Prune vines to remove diseased parts.",
        "4. Practice delayed pruning to reduce infection risk.",
        "5. Use resistant grape varieties if available."
    ],
    [
        "1. Apply fungicides like azoxystrobin or myclobutanil.",
        "2. Prune vines for better sunlight and air circulation.",
        "3. Remove and destroy infected leaves and canes.",
        "4. Apply sulfur sprays during the growing season.",
        "5. Avoid overhead irrigation to reduce leaf wetness."
    ],
    [
        "No specific treatment needed; maintain good vineyard management."
    ],
    [
        "1. Use insecticides to control citrus psyllids.",
        "2. Remove and destroy infected trees.",
        "3. Apply antibiotics like streptomycin if available.",
        "4. Practice integrated pest management (IPM) techniques.",
        "5. Plant disease-free nursery stock."
    ],
    [
        "1. Apply copper-based fungicides during the growing season.",
        "2. Prune trees to improve air circulation.",
        "3. Remove and destroy infected twigs and branches.",
        "4. Apply fixed copper sprays during dormant season.",
        "5. Avoid overhead irrigation to reduce disease spread."
    ],
    [
        "No specific treatment needed; maintain good orchard practices."
    ],
    [
        "1. Apply copper-based fungicides during the growing season.",
        "2. Rotate crops to reduce disease pressure.",
        "3. Use disease-resistant pepper varieties if available.",
        "4. Remove and destroy infected plant debris.",
        "5. Apply drip irrigation to avoid wetting foliage."
    ],
    [
        "No specific treatment needed; maintain good agricultural practices."
    ],
    [
        "1. Apply fungicides like chlorothalonil or mancozeb.",
        "2. Rotate crops to reduce disease build-up in soil.",
        "3. Remove and destroy infected foliage and tubers.",
        "4. Mulch around plants to prevent soil splashing.",
        "5. Use disease-resistant potato varieties if available."
    ],
    [
        "1. Apply fungicides like copper-based sprays or mancozeb.",
        "2. Practice crop rotation to break disease cycles.",
        "3. Remove and destroy infected plant parts promptly.",
        "4. Keep foliage dry by avoiding overhead irrigation.",
        "5. Apply protective fungicides preventively during humid weather."
    ],
    [
        "No specific treatment needed; maintain good agricultural practices."
    ],
    [
        "No specific treatment needed; maintain good orchard practices."
    ],
    [
        "No specific treatment needed; maintain good agricultural practices."
    ],
    [
        "1. Apply fungicides like sulfur or potassium bicarbonate.",
        "2. Remove and destroy infected leaves and vines.",
        "3. Prune plants to improve air circulation.",
        "4. Apply neem oil or horticultural oil to suppress fungal growth.",
        "5. Avoid overhead irrigation to reduce leaf wetness."
    ],
    [
        "1. Apply copper-based fungicides during the growing season.",
        "2. Remove and destroy infected leaves and runners.",
        "3. Prune plants to increase air circulation.",
        "4. Apply drip irrigation to keep foliage dry.",
        "5. Use disease-resistant strawberry varieties if available."
    ],
    [
        "No specific treatment needed; maintain good agricultural practices."
    ],
    [
        "1. Apply copper-based fungicides during the growing season.",
        "2. Rotate crops and practice good field hygiene.",
        "3. Remove and destroy infected plant debris.",
        "4. Apply drip irrigation to avoid wetting foliage.",
        "5. Use disease-resistant tomato varieties if available."
    ],
    [
        "1. Apply fungicides like chlorothalonil or mancozeb.",
        "2. Remove and destroy infected lower leaves and debris.",
        "3. Mulch around plants to prevent soil splashing.",
        "4. Practice crop rotation to reduce disease build-up.",
        "5. Keep foliage dry by watering at the base of plants."
    ],
    [
        "1. Apply fungicides like copper-based sprays or mancozeb.",
        "2. Remove and destroy infected leaves and plant debris.",
        "3. Practice crop rotation and avoid planting near infected areas.",
        "4. Ensure good air circulation around plants.",
        "5. Apply preventive sprays during periods of high humidity."
    ],
    [
        "1. Apply fungicides like chlorothalonil or copper-based sprays.",
        "2. Prune lower leaves to improve air circulation.",
        "3. Water plants at the base to keep foliage dry.",
        "4. Use mulch to prevent soil splashing onto leaves.",
        "5. Apply preventive sprays during cool, damp weather."
    ],
    [
        "1. Apply fungicides like chlorothalonil or mancozeb.",
        "2. Remove and destroy infected leaves and debris.",
        "3. Rotate crops and avoid overhead irrigation.",
        "4. Apply mulch to prevent soil splashing onto lower leaves.",
        "5. Use disease-resistant tomato varieties if available."
    ],
    [
        "1. Use miticides to control spider mite infestations.",
        "2. Increase humidity levels to discourage mite activity.",
        "3. Remove and destroy heavily infested plant parts.",
        "4. Apply insecticidal soap or neem oil to suppress mites.",
        "5. Use reflective mulches to deter mite movement."
    ],
    [
        "1. Apply fungicides like chlorothalonil or mancozeb.",
        "2. Remove and destroy infected plant debris.",
        "3. Practice crop rotation to reduce disease build-up.",
        "4. Maintain good air circulation around plants.",
        "5. Water plants at the base to avoid wetting foliage."
    ],
    [
        "1. Use insecticides to control whiteflies, the virus vector.",
        "2. Remove and destroy infected plants promptly.",
        "3. Use reflective mulches to deter whiteflies.",
        "4. Apply neem oil or insecticidal soap to suppress whiteflies.",
        "5. Plant resistant tomato varieties if available."
    ],
    [
        "1. Remove and destroy infected plants immediately.",
        "2. Control aphid populations, which can spread the virus.",
        "3. Use virus-free seed and disease-free transplants.",
        "4. Practice good field hygiene to reduce virus reservoirs.",
        "5. Avoid planting tomatoes near infected solanaceous plants."
    ],
    [
        "No specific treatment needed; maintain good agricultural practices."
    ]
]
    return plant_disease_cures[result]
 
#Navigation Bar
from streamlit_navigation_bar import st_navbar
page = st_navbar(["Home","Scanner","PhytoGuard", "About"])
# Custom CSS to move the navigation bar to the rightmost corner
st.markdown(
    """
    <style>
    .stNavBar {
        position: fixed;
        top: 0;
        right: 0;
        background-color: #f0f0f0;  /* Adjust background color as needed */
        padding: 10px;
        z-index: 1; /* Ensure it's above other content */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Home Page
if page == "Home":
    st.markdown("""
        <style>
            .title {
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)
    st.markdown("<h1 class='title'>LeafGuardian</h1>", unsafe_allow_html=True)
    
    #Lottie
    lottie_scanner = load_lottiefile("lotiie/First Project/tree_grow.json")
    st_lottie(
        lottie_scanner,
        key = "None",
    )
    st.markdown("""
                # Welcome to LeafGuardian

**LeafGuardian** is your go-to solution for identifying and managing plant diseases. Our cutting-edge technology uses advanced machine learning models to analyze images of plant leaves and provide accurate diagnoses and effective treatment recommendations.

## Key Features

- **Instant Disease Recognition**: Simply upload a photo of your plant's leaves, and our AI-powered system will quickly identify any diseases.
- **Detailed Disease Information**: Get comprehensive information about the detected diseases, including symptoms, causes, and preventive measures.
- **Personalized Treatment Plans**: Receive tailored treatment suggestions to help you manage and cure plant diseases effectively.
- **User-Friendly Interface**: Easy-to-use platform designed for gardeners, farmers, and plant enthusiasts of all skill levels.

## How It Works

1. **Upload an Image**: Take a clear photo of the affected plant leaf and upload it using our user-friendly interface.
2. **Get Instant Results**: Our AI model will analyze the image and identify any potential diseases.
3. **Receive Recommendations**: Access detailed information about the disease and get personalized treatment recommendations.

## Why Choose LeafGuardian?

- **Accuracy**: Our models are trained on a vast dataset of plant images to ensure high accuracy in disease detection.
- **Speed**: Get results in seconds, helping you take quick action to save your plants.
- **Reliability**: Trusted by gardeners, farmers, and agricultural professionals around the world.

""")
    st.markdown("""
---



Thank you for choosing LeafGuardian. Together, we can keep your plants healthy and thriving!


                """)
        
# Leaf Scanner Page
elif page == "Scanner":
    st.markdown("""
        <style>
            .title {
                text-align: center;
            }
        </style>
    """, unsafe_allow_html=True)
    

    
    lottie_scanner = load_lottiefile("lotiie/First Project/leaf_scan.json")
    st_lottie(
        lottie_scanner,
        key = "None",
    )
    st.write("## Instructions:")
    st.write("1. Upload an image of your plant's leaf using the button below.")
    st.write("2. Alternatively, you can use the camera option to take a photo directly.")
    st.write("3. Click the 'Analyze' button to receive results and recommended treatments based on the analysis.")
    
# Camera Input
    test_image_camera = st.camera_input("Take a Picture")
    
    # File Uploader
    test_image_upload = st.file_uploader("Choose File", type=["jpg", "jpeg", "png"])
    
    #This Buttom Will Show The Image    
    if st.button("Show Image"):
        if test_image_camera:
            st.image(test_image_camera, caption='Selected Image.', use_column_width=True)
        elif test_image_upload:
            st.image(test_image_upload, caption='Selected Image.', use_column_width=True)
        else:
            st.write("Please capture an image or upload a file first.")
    
    
            # Predict Button
           # Predict and Show Image Button
    if st.button("Predict"):
        if test_image_camera:
        # Perform prediction on test_image_camera
            index_prediction = model_prediction(test_image_camera)
            disease_name = diseases(index_prediction)
            st.markdown(f"**Disease:** '{disease_name}'")
            st.markdown("**Cure Recommendations:**")
            for point in cure(index_prediction):
              st.write(point)
        elif test_image_upload:
        # Perform prediction on test_image_upload
           index_prediction = model_prediction(test_image_upload)
           disease_name = diseases(index_prediction)
           st.markdown(f"**Disease:** {disease_name}")
           st.markdown("**Cure Recommendations:**")
           for point in cure(index_prediction):
             st.write(point)
    else:
        st.write("Please capture an image or upload a file first.")
        
    st.markdown("""
---



Thank you for choosing LeafGuardian. Together, we can keep your plants healthy and thriving!


                """)
    
# Leaf Guide
elif page == "PhytoGuard":
    lottie_scanner = load_lottiefile("lotiie/First Project/moving_peatle.json")
    st_lottie(
        lottie_scanner,
        key = "None",
    )
    st.markdown("""
                **LeafGuardian** is your go-to solution for identifying and managing plant diseases. Our cutting-edge technology uses advanced machine learning models to analyze images of plant leaves and provide accurate diagnoses and effective treatment recommendations.

## Diseases

### Apple Scab

**Cause:** Apple scab, caused by the fungus *Venturia inaequalis*, thrives in cool, wet weather conditions. It infects apple trees through airborne spores, forming dark, scabby lesions on leaves and fruit.

**Symptoms:** Dark, olive-green spots on leaves and fruit, leading to defoliation and reduced fruit quality.

**Management:**
- Prune affected branches to improve airflow.
- Apply fungicides before rainy periods.
- Plant resistant apple varieties such as 'Liberty' or 'Enterprise'.

---

### Apple Black Rot

**Cause:** Apple black rot, caused by the fungus *Botryosphaeria obtusa*, infects apples during wet, warm weather. It spreads through spores in rain and wind.

**Symptoms:** Circular, sunken lesions on fruit and leaves, which turn brown and develop black rings. Fruit mummifies and shrivels.

**Management:**
- Remove and destroy infected fruit.
- Apply fungicides during bloom and fruit development stages.
- Maintain good orchard hygiene to reduce overwintering spores.

---

### Cedar Apple Rust

**Cause:** Cedar apple rust, caused by the fungus *Gymnosporangium juniperi-virginianae*, requires both apple and cedar trees for its life cycle. It spreads through airborne spores.

**Symptoms:** Bright orange-yellow spots on leaves and fruit. Spots enlarge and turn brown, causing leaf distortion and premature defoliation.

**Management:**
- Remove nearby cedar trees if possible.
- Apply fungicides during wet weather.
- Plant resistant apple varieties.

---

### Cherry Powdery Mildew

**Cause:** Powdery mildew, caused by various fungi like *Podosphaera clandestina*, thrives in warm, dry conditions. It spreads through airborne spores.

**Symptoms:** White powdery patches on leaves and shoots, which may distort growth and reduce fruit quality.

**Management:**
- Plant resistant cherry varieties.
- Apply fungicides preventively.
- Improve air circulation around plants.

---

### Corn Cercospora Leaf Spot / Gray Leaf Spot

**Cause:** Cercospora leaf spot and gray leaf spot, caused by the fungus *Cercospora zeae-maydis* and *Cercospora zeina*, respectively, thrive in warm, humid conditions. They spread through splashing water or windborne spores.

**Symptoms:** Small, gray to brown lesions with yellow halos on leaves. Lesions may coalesce, leading to extensive leaf blighting.

**Management:**
- Rotate crops to break disease cycles.
- Apply fungicides preventively during early stages of infection.
- Maintain plant health with adequate spacing and balanced nutrition.

---

### Corn Common Rust

**Cause:** Common rust, caused by the fungus *Puccinia sorghi*, thrives in warm, humid conditions. It spreads rapidly through airborne spores.

**Symptoms:** Small, circular, powdery orange pustules on leaves. Severe infections can cause premature leaf senescence and yield loss.

**Management:**
- Plant resistant corn varieties if available.
- Apply fungicides at the first sign of infection.
- Practice crop rotation and remove crop debris.

---

### Corn Northern Leaf Blight

**Cause:** Northern leaf blight, caused by the fungus *Exserohilum turcicum*, prefers warm, humid conditions. It spreads through windborne spores and thrives on maize residues.

**Symptoms:** Large, cigar-shaped lesions with wavy edges on leaves. Lesions may merge, leading to extensive blighting and reduced photosynthesis.

**Management:**
- Plant resistant corn hybrids.
- Apply fungicides preventively during periods of high humidity.
- Practice crop rotation and residue management.

---

### Grape Black Rot

**Cause:** Black rot, caused by the fungus *Guignardia bidwellii*, thrives in warm, humid conditions. It spreads through airborne spores.

**Symptoms:** Circular, expanding brown lesions on leaves and fruit. Fruit may shrivel and mummify.

**Management:**
- Prune vines to improve air circulation.
- Apply fungicides preventively during critical growth stages.
- Remove and destroy infected plant material.

---

### Grape Esca (Black Measles)

**Cause:** Esca, caused by several fungal species including *Phaeoacremonium spp.*, *Phaeomoniella chlamydospora*, and *Fomitiporia mediterranea*, infects grapes through pruning wounds or natural openings. It can also spread through airborne spores.

**Symptoms:** Chlorosis (yellowing) between leaf veins, brown streaks in wood, and black spots on berries. Vines may exhibit dieback symptoms.

**Management:**
- Use certified disease-free planting material.
- Practice careful pruning to avoid wounds.
- Apply preventive fungicides and maintain good vineyard hygiene.

---

### Grape Leaf Blight (Isariopsis Leaf Spot)

**Cause:** Isariopsis leaf spot, caused by *Isariopsis griseola*, thrives in warm, humid conditions. It spreads through windborne spores.

**Symptoms:** Small, round, reddish-brown spots on leaves. Spots may coalesce and cause defoliation in severe cases.

**Management:**
- Plant resistant grape varieties.
- Apply fungicides preventively during wet weather.
- Improve vineyard ventilation and spacing.

---

### Orange Haunglongbing (Citrus Greening)

**Cause:** Citrus greening, caused by the bacterium *Candidatus Liberibacter spp.*, is transmitted by the Asian citrus psyllid (*Diaphorina citri*). It affects citrus trees by blocking nutrient flow, leading to yellow shoots, misshapen fruits, and eventual decline.

**Symptoms:** Yellow shoots, mottled leaves, small and bitter fruits with uneven coloring (greening), and premature fruit drop.

**Management:**
- Control psyllid populations through insecticide applications.
- Use certified disease-free planting material.
- Remove and destroy infected trees to prevent spread.

---

### Peach Bacterial Spot

**Cause:** Bacterial spot, caused by *Xanthomonas arboricola* pv. *pruni*, thrives in warm, humid conditions. It spreads through rain splashes and pruning tools.

**Symptoms:** Small, water-soaked lesions on leaves, which turn dark and necrotic. Lesions may also appear on fruits, causing fruit deformation and reduced quality.

**Management:**
- Prune to improve air circulation.
- Apply copper-based fungicides during bud break and rainy periods.
- Avoid overhead irrigation to reduce leaf wetness.

---

### Pepper, Bell Bacterial Spot

**Cause:** Bacterial spot, caused by *Xanthomonas campestris* pv. *vesicatoria*, affects bell peppers and other capsicum species. It spreads through rain splashes, wind, and contaminated tools.

**Symptoms:** Small, water-soaked lesions on leaves, which turn brown with yellow halos. Lesions may also appear on fruits, causing spots and lesions.

**Management:**
- Rotate crops to break disease cycles.
- Apply copper-based fungicides preventively.
- Practice good field hygiene and avoid working in wet conditions.

---

### Potato Early Blight

**Cause:** Early blight, caused by the fungus *Alternaria solani*, thrives in warm, humid conditions. It overwinters in soil and plant debris, spreading through windborne spores.

**Symptoms:** Dark, concentric rings with yellow halos on leaves, starting from lower leaves. Lesions may coalesce, causing premature defoliation and reduced tuber yield.

**Management:**
- Rotate crops and practice crop rotation.
- Apply fungicides preventively during periods of leaf wetness.
- Remove and destroy infected plant debris.

---

### Potato Late Blight

**Cause:** Late blight, caused by the fungus *Phytophthora infestans*, thrives in cool, moist conditions. It spreads rapidly through windborne spores and can cause devastating epidemics.

**Symptoms:** Dark, water-soaked lesions on leaves, which turn brown and necrotic. White mold may appear under humid conditions. Infected tubers develop dark, firm lesions.

**Management:**
- Plant resistant potato varieties if available.
- Apply fungicides preventively during cool, wet weather.
- Practice crop rotation and remove infected plant debris.

---

### Squash Powdery Mildew

**Cause:** Powdery mildew, caused by various fungi like *Podosphaera xanthii*, thrives in warm, dry conditions. It spreads through windborne spores.

**Symptoms:** White powdery patches on leaves, which may cover leaf surfaces and cause leaf curling and yellowing. Severe infections can lead to stunted growth and reduced fruit production.

**Management:**
- Plant resistant squash varieties if available.
- Apply fungicides preventively during early stages of infection.
- Improve air circulation and avoid overhead irrigation.

---

### Strawberry Leaf Scorch

**Cause:** Leaf scorch, caused by the bacterium *Xylella fastidiosa*, affects strawberry plants by blocking water flow in xylem vessels. It is spread by insects like sharpshooters.

**Symptoms:** Reddish-purple discoloration along leaf margins, which progresses to necrosis. Leaves may become brittle and curl upward.

**Management:**
- Control insect vectors through insecticide applications.
- Use disease-free planting material.
- Remove and destroy infected plants to prevent spread.

---

### Tomato Bacterial Spot

**Cause:** Bacterial spot, caused by *Xanthomonas spp.*, affects tomato plants in warm, humid conditions. It spreads through rain splashes, wind, and contaminated tools.

**Symptoms:** Small, water-soaked lesions on leaves, which turn brown with yellow halos. Lesions may also appear on fruits, causing spots and lesions.

**Management:**
- Rotate crops to break disease cycles.
- Apply copper-based fungicides preventively.
- Practice good field hygiene and avoid working in wet conditions.

---

### Tomato Early Blight

**Cause:** Early blight, caused by the fungus *Alternaria solani*, thrives in warm, humid conditions. It overwinters in soil and plant debris, spreading through windborne spores.

**Symptoms:** Dark, concentric rings with yellow halos on leaves, starting from lower leaves. Lesions may coalesce, causing premature defoliation and reduced fruit yield.

**Management:**
- Rotate crops and practice crop rotation.
- Apply fungicides preventively during periods of leaf wetness.
- Remove and destroy infected plant debris.

---

### Tomato Late Blight

**Cause:** Late blight, caused by the oomycete *Phytophthora infestans*, thrives in cool, wet conditions. It spreads rapidly through windborne spores and can cause devastating epidemics.

**Symptoms:** Dark, water-soaked lesions on leaves, which turn brown and necrotic. White mold may appear under humid conditions. Infected fruits develop dark, firm lesions.

**Management:**
- Plant resistant tomato varieties if available.
- Apply fungicides preventively during cool, wet weather.
- Practice crop rotation and remove infected plant debris.

---

### Tomato Leaf Mold

**Cause:** Leaf mold, caused by the fungus *Fulvia fulva* (formerly *Cladosporium fulvum*), thrives in warm, humid conditions. It spreads through windborne spores.

**Symptoms:** Pale yellow to brown patches on leaves, usually starting from lower leaves. Fuzzy white or gray mold may appear on the underside of leaves.

**Management:**
- Maintain good air circulation and spacing between plants.
- Avoid overhead irrigation to reduce leaf wetness.
- Apply fungicides preventively during periods of high humidity.

---

### Tomato Septoria Leaf Spot

**Cause:** Septoria leaf spot, caused by *Septoria lycopersici*, thrives in warm, humid conditions. It spreads through rain splashes and contaminated tools.

**Symptoms:** Small, circular lesions with dark borders and gray centers on leaves. Lesions may coalesce and cause defoliation, reducing fruit quality and yield.

**Management:**
- Remove infected leaves promptly.
- Apply fungicides preventively during wet weather.
- Improve air circulation and avoid overhead irrigation.

---

### Tomato Spider Mites / Two-Spotted Spider Mite

**Cause:** Spider mites, including the two-spotted spider mite (*Tetranychus urticae*), feed on tomato plants by piercing leaf cells and sucking sap. They thrive in hot, dry conditions and can quickly reproduce, leading to population explosions.

**Symptoms:** Fine webbing on leaves, stippling (tiny yellow or white spots) on leaves, and leaf discoloration. Severe infestations cause leaf curling, premature leaf drop, and reduced fruit yield.

**Management:**
- Use insecticidal soaps or horticultural oils to control mite populations.
- Introduce predatory mites or beneficial insects.
- Maintain plant health with adequate watering and nutrient supply.

---

### Tomato Target Spot

**Cause:** Target spot, caused by *Corynespora cassiicola*, thrives in warm, humid conditions. It spreads through rain splashes and windborne spores.

**Symptoms:** Circular to angular lesions with concentric rings on leaves. Lesions may have a target-like appearance with dark centers and yellow halos. Severe infections cause defoliation and reduced fruit quality.

**Management:**
- Rotate crops and practice crop residue removal.
- Apply fungicides preventively during periods of leaf wetness.
- Improve air circulation and avoid overhead irrigation.

---

### Tomato Yellow Leaf Curl Virus

**Cause:** Yellow leaf curl virus, transmitted by whiteflies (*Bemisia tabaci*), infects tomatoes and other solanaceous plants. The virus disrupts plant growth and reduces fruit yield.

**Symptoms:** Yellowing and upward curling of leaves, stunted plant growth, and leaf distortion. Infected plants may produce fewer and smaller fruits.

**Management:**
- Control whitefly populations through insecticide applications.
- Use virus-resistant tomato varieties if available.
- Remove and destroy infected plants to prevent spread.

---

### Tomato Mosaic Virus

**Cause:** Tomato mosaic virus (ToMV), transmitted through contaminated tools, hands, or plant sap, infects tomatoes and related plants. It can survive in infected plant debris and seeds.

**Symptoms:** Mottled or streaked yellow patterns on leaves, leaf curling, and stunted growth. Fruits may show mottling, spots, or streaks, reducing marketability.

**Management:**
- Use disease-free seeds and virus-tested transplants.
- Practice strict sanitation to avoid virus spread.
- Remove and destroy infected plants and debris promptly.

---



Thank you for choosing LeafGuardian. Together, we can keep your plants healthy and thriving!


                """)

# About Page
elif page == "About":
    lottie_scanner = load_lottiefile("lotiie/First Project/hi_eye.json")
    st_lottie(
        lottie_scanner,
        key="None",
    )
    st.markdown("""
                # About

Welcome to Leaf Guardian! I'm **Aditya Sarkar**, the creator of this project. As a passionate plant enthusiast and tech aficionado, I developed Leaf Guardian to help gardeners, farmers, and plant lovers like myself keep their plants healthy and thriving.

## Background

I created LeafGuardian based on my experiences with plant care and my background in [your field, e.g., computer science, machine learning]. I wanted to develop a reliable tool that leverages advanced technology to solve common plant care challenges.

## Contact Information

Feel free to reach out to me on social media or via email. I'd love to hear your feedback and suggestions!

- **Email**: adi.sarkar2004@gmail.com
- **Email**: +91 8989028700

                """)
    st.markdown("""
    <style>
        .social-icons {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px; /* Adjust the gap between icons if needed */
        }
        .social-icons .icon {
            margin: 0 10px;
        }
    </style>
    <div class="social-icons">
        <a href="https://www.linkedin.com/in/aditya-sarkar-a7a321206/" target="_blank" class="icon">
            <img src="https://img.icons8.com/color/48/000000/linkedin.png"/>
        </a>
        <a href="https://www.instagram.com/adi_jong_un/" target="_blank" class="icon">
            <img src="https://img.icons8.com/color/48/000000/instagram-new.png"/>
        </a>
        <a href="https://github.com/SarkariKill" target="_blank" class="icon">
            <img src="https://img.icons8.com/material-rounded/48/000000/github.png"/>
        </a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
---



Thank you for choosing LeafGuardian. Together, we can keep your plants healthy and thriving!


                """)
    

    




