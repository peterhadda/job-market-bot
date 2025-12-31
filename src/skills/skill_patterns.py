SKILL_ALIASES = {

    # =====================
    # Programming
    # =====================
    "python": ["python"],
    "java": ["java"],
    "r": ["r language", "r programming"],
    "scala": ["scala"],

    # =====================
    # Data & Databases
    # =====================
    "sql": ["sql", "postgresql", "postgres", "mysql", "sqlite", "t-sql", "tsql", "mssql", "sql server"],
    "nosql": ["nosql", "mongodb", "cassandra", "redis", "dynamodb"],
    "data modeling": ["data modeling", "data modelling", "dimensional modeling", "star schema", "snowflake schema"],
    "data warehouse": ["data warehouse", "data warehousing", "dw", "dwh"],
    "etl": ["etl", "elt", "data pipeline", "data pipelines"],
    "pandas": ["pandas"],
    "numpy": ["numpy"],
    "spark": ["spark", "pyspark", "apache spark"],
    "hadoop": ["hadoop"],
    "dbt": ["dbt", "data build tool"],
    "snowflake": ["snowflake"],
    "bigquery": ["bigquery", "big query"],
    "redshift": ["redshift", "amazon redshift"],

    # =====================
    # Streaming / Messaging (Data Engineering)
    # =====================
    "kafka": ["kafka", "apache kafka"],
    "rabbitmq": ["rabbitmq"],
    "streaming": ["streaming", "real-time data", "realtime data"],

    # =====================
    # Statistics & Math
    # =====================
    "statistics": ["statistics", "statistical analysis"],
    "probability": ["probability", "probabilistic", "bayesian", "bayes", "bayesian inference"],
    "linear algebra": ["linear algebra"],
    "optimization": ["optimization", "optimisation"],
    "time series": ["time series", "forecasting", "arima", "prophet"],

    # =====================
    # Machine Learning
    # =====================
    "machine learning": ["machine learning", "ml"],
    "deep learning": ["deep learning", "dl"],
    "scikit-learn": ["scikit-learn", "sklearn", "scikit learn"],
    "xgboost": ["xgboost"],
    "lightgbm": ["lightgbm"],
    "catboost": ["catboost"],

    # =====================
    # NLP & Vision
    # =====================
    "nlp": ["nlp", "natural language processing"],
    "computer vision": ["computer vision"],
    "opencv": ["opencv"],
    "transformers": ["transformers", "hugging face", "huggingface", "bert", "gpt", "llm", "large language model", "large language models"],
    "prompt engineering": ["prompt engineering", "prompt design"],

    # =====================
    # DL Frameworks
    # =====================
    "tensorflow": ["tensorflow"],
    "keras": ["keras"],
    "pytorch": ["pytorch", "torch"],

    # =====================
    # ML Evaluation & Experimentation
    # =====================
    "model evaluation": ["model evaluation", "evaluation metrics", "metrics"],
    "cross validation": ["cross validation", "cross-validation", "cv"],
    "hyperparameter tuning": ["hyperparameter tuning", "hyperparameter optimization", "hyperparameter optimisation"],
    "ab testing": ["a/b testing", "ab testing", "experiment design"],
    "feature engineering": ["feature engineering"],
    "data quality": ["data quality", "data validation"],

    # =====================
    # MLOps / Deployment
    # =====================
    "mlflow": ["mlflow"],
    "airflow": ["airflow", "apache airflow"],
    "docker": ["docker", "docker-compose", "docker compose"],
    "kubernetes": ["kubernetes", "k8s"],
    "ci/cd": ["ci/cd", "cicd", "continuous integration", "continuous delivery", "continuous deployment"],
    "fastapi": ["fastapi"],
    "flask": ["flask"],
    "rest api": ["rest api", "restful", "restful api", "api development"],
    "graphql": ["graphql"],

    # =====================
    # Cloud
    # =====================
    "aws": ["aws", "amazon web services"],
    "azure": ["azure", "microsoft azure"],
    "gcp": ["gcp", "google cloud", "google cloud platform"],

    # =====================
    # Data Visualization & BI
    # =====================
    "tableau": ["tableau"],
    "power bi": ["power bi", "powerbi"],
    "excel": ["excel", "microsoft excel"],
    "matplotlib": ["matplotlib"],
    "seaborn": ["seaborn"],
    "plotly": ["plotly"],

    # =====================
    # OS & Tools
    # =====================
    "linux": ["linux", "unix"],
    "bash": ["bash", "shell", "shell scripting"],
    "git": ["git", "github", "gitlab", "bitbucket"],

    # =====================
    # Marketing (Core)
    # =====================
    "marketing": ["marketing", "digital marketing"],
    "content marketing": ["content marketing", "content strategy"],
    "email marketing": ["email marketing", "email campaigns", "newsletter"],
    "social media marketing": ["social media marketing", "social media", "smm"],
    "seo": ["seo", "search engine optimization"],
    "sem": ["sem", "search engine marketing"],
    "ppc": ["ppc", "pay per click", "paid ads", "paid advertising"],
    "growth marketing": ["growth marketing", "growth hacking"],
    "brand management": ["brand management", "branding"],
    "campaign management": ["campaign management", "marketing campaigns"],
    "copywriting": ["copywriting", "marketing copy"],
    "influencer marketing": ["influencer marketing", "influencers"],

    # =====================
    # Marketing Analytics / Growth
    # =====================
    "marketing analytics": ["marketing analytics", "campaign analytics"],
    "attribution modeling": ["attribution modeling", "marketing attribution"],
    "conversion rate optimization": ["conversion rate optimization", "cro"],
    "funnel analysis": ["funnel analysis", "conversion funnel"],
    "user acquisition": ["user acquisition", "customer acquisition"],
    "retention": ["retention", "customer retention"],
    "churn analysis": ["churn", "churn analysis"],
    "lifetime value": ["lifetime value", "ltv", "clv"],
    "customer segmentation": ["customer segmentation", "segmentation"],
    "cohort analysis": ["cohort analysis"],

    # =====================
    # Product & Strategy
    # =====================
    "product management": ["product management", "product manager", "pm"],
    "product analytics": ["product analytics"],
    "roadmapping": ["roadmap", "product roadmap"],
    "go-to-market": ["go to market", "gtm"],
    "pricing strategy": ["pricing strategy", "pricing"],
    "market research": ["market research", "competitive analysis"],
    "user research": ["user research", "ux research"],

    # =====================
    # Sales / CRM / Revenue
    # =====================
    "sales": ["sales", "b2b sales", "b2c sales"],
    "crm": ["crm", "customer relationship management"],
    "salesforce": ["salesforce"],
    "hubspot": ["hubspot"],
    "lead generation": ["lead generation", "lead gen"],
    "lead scoring": ["lead scoring"],
    "pipeline management": ["pipeline management", "sales pipeline"],
    "revenue analysis": ["revenue analysis", "revenue modeling"],
    "forecasting": ["forecasting", "sales forecasting"],

    # =====================
    # Business & Operations
    # =====================
    "business strategy": ["business strategy", "strategic planning"],
    "operations": ["operations", "business operations"],
    "process improvement": ["process improvement", "process optimization"],
    "kpis": ["kpi", "kpis", "key performance indicators"],
    "okrs": ["okrs", "objectives and key results"],
    "budgeting": ["budgeting", "budget management"],
    "financial analysis": ["financial analysis", "financial modeling"],
    "profitability": ["profitability", "margin analysis"],
    "cost analysis": ["cost analysis"],

    # =====================
    # Consulting / Client-facing
    # =====================
    "consulting": ["consulting", "management consulting"],
    "client management": ["client management", "client relations"],
    "presentations": ["presentations", "executive presentations"],
    "storytelling": ["storytelling", "data storytelling"],
    "change management": ["change management"],

    # =====================
    # Compliance / Security (non-coding but common)
    # =====================
    "privacy": ["privacy", "data privacy", "pii", "gdpr"],
    "security": ["security", "information security", "infosec"],
    # =====================
    # Education / Teaching
    # =====================
    "teaching": ["teaching", "teaching experience"],
    "education": ["education", "educational background"],
    "teacher": ["teacher", "school teacher", "high school teacher"],
    "lecturer": ["lecturer", "instructor"],
    "professor": ["professor", "faculty member"],
    "tutoring": ["tutoring", "tutor"],
    "training": ["training", "employee training", "staff training"],
    "curriculum development": ["curriculum development", "lesson planning"],
    "classroom management": ["classroom management"],
    "assessment": ["assessment", "student assessment", "grading"],

    # =====================
    # Graduate / Entry-Level
    # =====================
    "graduate": ["graduate", "recent graduate", "new graduate"],
    "entry level": ["entry level", "entry-level", "junior level"],
    "junior": ["junior", "junior role", "junior position"],
    "internship": ["internship", "intern", "internship experience"],
    "co-op": ["co-op", "coop", "cooperative education"],
    "trainee": ["trainee", "graduate trainee"],
    "apprenticeship": ["apprenticeship", "apprentice"],
    "academic projects": ["academic projects", "university projects"],

    # =====================
    # Client / Customer Service
    # =====================
    "customer service": ["customer service", "customer support", "customer care"],
    "client service": ["client service", "client services"],
    "client support": ["client support"],
    "customer success": ["customer success"],
    "account management": ["account management", "account manager"],
    "client relations": ["client relations", "client relationship management"],
    "customer relations": ["customer relations"],
    "help desk": ["help desk", "service desk"],
    "technical support": ["technical support", "tech support"],
    "call center": ["call center", "contact center"],

    # =====================
    # Hospitality / Service-Oriented Roles (optional but common)
    # =====================
    "hospitality": ["hospitality"],
    "front desk": ["front desk", "reception"],
    "guest services": ["guest services"],
    "service excellence": ["service excellence"]

}
