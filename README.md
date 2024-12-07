# Financial Institution Moral Foundations Survey Analysis 💸
A financial institution in Washington has become concerned that their current membership 
base is not well-aligned with their corporate values. Through that concern they 
realized that don't actually understand their membership's values very well. They 
surveyed 2,421 members to shed light on the issue. 

The heart of the survey was the Moral Foundations Theory of Jonathan Haidt. Members 
were surveyed on the Moral Foundations Questionnaire, which you should take so you 
understand the test. Survey respondents were scored on the five foundations as well 
as a single-number summary, Progressivism. 

The financial institution values Localism, Sustainability, and Education. These aspects 
of member's values were assessed in the survey as well. Localism and Sustainability used
validated scales and thus can be summarized via a single score, where higher values indicate
greater support for the values. Education is summarized by the following three questions, 
which we do not have evidence can be combined into a single score:

* In general, public schools provide a better education than private schools.
* Public school teachers are underpaid.
* Experience is more important than education in determining success in life.
These questions were evaluated on a 1 to 6 scale where 1 indicated "Strongly Disagree" and 
6 indicated "Strongly Agree". 

Finally, we have information on the member that can be used to understand variation 
in their values. 



# Assignment Results


### Demographic Clustering

__I used four clusters, arbitrarily, for this analysis.__

__How evenly do your clusters align with the regions?__

None of my clusters appear to be confined to a single region. All clusters span multiple areas, suggesting that regional factors do not significantly influence age, gender, engagement, or account age.

Briefly describe the clusters. 

Cluster:
* Zero: Highly engaged only. Account age is between 0 and 30. User age is between 18 and 80. All genders. 
* One: All levels of engagement. Account age is between 10 and 50. User age is between 40 and 95. All genders.
* Two: Only engaged and not engaged. Account age is between 0 and 33. User age is between 18 and 85. Only males.
* Three: Only engaged and not engaged. Account age is between 0 and 33. User age is between 18 and 95. Only females and other.

I [used a cluster 'dashboard'](cluster_exploration_dashboard.ipynb) to explore the focal values of the clusters. It utilizes both 2-D and 3-D Dashboard to visualize the data by the different features. 

![alt text](assets/3-d_agefaircluster.png)


### Values Clustering
After you’ve built your clusters, report the following information on each cluster:

* Predominant region
* Average age and account age
* Most common focal value
* Mean results on the questions of `pub.greater.priv`, `experience.more.important`, and `teachers.underpaid`. 

Each of my clusters encompasses various regions; there is no single predominant region for any of the clusters. 

![Average Age and Acount Age](assets/2024-10-27%2017_48_45-Window.png)

Most Common Focal Values:
* Zero: Environment
* One: Health (i.e. cancer research)
* Two: Health (i.e. cancer research)
* Three: Education                         
* Four: Education                         


![Mean results on the questions](<assets/2024-10-27 17_52_15-Window.png>)


## Workflow

```mermaid
    graph TD;
        A[Start] --> B[Load Data]
        B --> C[Preprocess Data]
        C --> D[Normalize Data]
        D --> E[Set Up K-Means Model]
        E --> F[Fit and Predict Clusters]
        F --> G[Analyze Clusters]
        G --> H[Visualize Results]
        H --> I[Iterate and Refine]

        subgraph Clustering Assignment.ipynb
            B
            C
            D
            E
            F
            G
            H
        end

        subgraph clustering_code.py
            J[Functions for K-Means Clustering]
            J --> E
        end

        subgraph linear_algebra.py
            K[Linear Algebra Functions]
            K --> D
        end

        subgraph scikit-learn-Kmeans-cluster-docs
            L[Reference for KMeans]
            L --> E
        end
```

## Feedback
Great work on this. I your write-up is thorough and engaging, as usual. It's interesting that we don't see much regional alignment. Typically I see a bit more of that. Regardless, great work. 

## ADA Clustering In-Class & Assignment

This repo holds the clustering code that we'll use in class and will
also be the place you put your clustering assignment. I have included
code that does clustering both in Python and R. 

This repo includes the following files: 

* `Clustering Assignment.ipynb`: This is the assignment for this week.
* `Clustering Surveys.ipynb`: We'll go through this code in class.
* `Clustering Surveys-Solutions.ipynb`: The solutions to the in-class work. 
* `cluster_exploration_dashboard.ipynb`: Dashboards for cluster exploration. Has 2-d and 3-d dashboards.
* `clustering_code.py`: Helper functions from "Data Science from Scratch" that
perform K-means clustering. 
* `linear_algebra.py`: More code from DSFS, which has the needed linear algebra
functions that we use. 
* `r-examples/`: A folder that holds R versions of all of this code. 
* `survey_responses.txt`: The results of annual class surveys, building up 
a data set to perform clustering on. I'll post an updated version to Moodle 
if more results come in. 
* `washington_survey_data.txt`: Data for the assignment.

## Data Dictionary

The data consists of the following columns:

* ID: a unique identifier for the survey respondent.
* age: the age of the respondent.
* gender: gender was evaluated with robust scale and collapsed into male/female/other for 
  those whose gender identity was not male or female.
* engagement: three categories of engagement with the financial institution.
* mem.edu: the self-reported education level of the member with the following scale:
* zip: the member zip code. 
* channel: how the member joined the financial institution. Options are "Loan" if they joined 
  via an auto loan, "Branch" if they joined at a branch and other for online or unknown. 
* progressivism/harm/fair/in.group/authority/purity: The MFQ results.
* account.age: the age of the member's account, in years. 
* region: The region of Washington the member lives in. May be easier to work with than zip.
* public.sector: has the person ever been a public employee?
* sustainability/localism: Scores on the validated scales. Higher values indicate greater
  support for the value.
* pub.greater.priv/experience.more.important/teachers.underpaid: The responses to the 
  education questions above. 
* main.focal.value: Respondents were asked, "Below is a list of broad areas to which people 
  often dedicate their volunteer or philanthropic efforts. From this list, please select the 
  most important to you. If an area of particular importance is missing, please let us know 
  about it in the space for 'other.'" This column holds the respondents' answer to that question.
* support.of.focal.value: Respondents were given an opportunity to indicate how they 
  supported their focal value. Those responses were collapsed into a single score, where 
  a higher value indicates more support.


