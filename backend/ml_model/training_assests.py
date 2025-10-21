import pandas as pd
import random
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from career_data import CAREER_REQUIREMENTS, SKILLS_LIST, INTERESTS_LIST, EDUCATION_LEVELS, WORK_STYLES



data = []
for career, details in CAREER_REQUIREMENTS.items():
    for _ in range(25):  # multiple examples per career
        skills = random.sample(details["required_skills"], min(len(details["required_skills"]), random.randint(2, 5)))
        interest = random.choice(details["interests"])
        education = random.choice(details["education"])
        work_style = random.choice(details["work_style"])

        data.append({
            "skills": ', '.join(skills),
            "interest": interest,
            "education": education,
            "work_style": work_style,
            "career": career
        })

df = pd.DataFrame(data)
df.to_csv("training_data.csv", index=False)
print(f"✅ training_data.csv created with {len(df)} records")



label_encoder = LabelEncoder()
education_encoder = LabelEncoder()
work_style_encoder = LabelEncoder()
interest_encoder = LabelEncoder()


df["career_encoded"] = label_encoder.fit_transform(df["career"])
df["education_encoded"] = education_encoder.fit_transform(df["education"])
df["work_style_encoded"] = work_style_encoder.fit_transform(df["work_style"])
df["interest_encoded"] = interest_encoder.fit_transform(df["interest"])


all_skills = sorted(list({skill for cat in SKILLS_LIST.values() for skill in cat}))
for skill in all_skills:
    df[skill] = df["skills"].apply(lambda x: 1 if skill in x else 0)



feature_cols = ["education_encoded", "work_style_encoded", "interest_encoded"] + all_skills
X = df[feature_cols]
y = df["career_encoded"]

model = DecisionTreeClassifier(max_depth=8, random_state=42)
model.fit(X, y)
print("✅ Model trained successfully")


with open("trained_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)

with open("education_encoder.pkl", "wb") as f:
    pickle.dump(education_encoder, f)

with open("work_style_encoder.pkl", "wb") as f:
    pickle.dump(work_style_encoder, f)

with open("skills_list.pkl", "wb") as f:
    pickle.dump(all_skills, f)

with open("interests_list.pkl", "wb") as f:
    pickle.dump(INTERESTS_LIST, f)

print("✅ All pickle files generated successfully:")
print("   - trained_model.pkl")
print("   - label_encoder.pkl")
print("   - education_encoder.pkl")
print("   - work_style_encoder.pkl")
print("   - skills_list.pkl")
print("   - interests_list.pkl")
