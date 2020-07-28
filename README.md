# Hi there 👋

<details open><summary>Python</summary>
<p>

```python
class AaronReidSmith:
    def __init__(self):
        self.username = 'aaronreidsmith'
        self.name = 'Aaron Smith'
        self.email = 'aaronreidsmith@gmail.com'
        self.social = {
            'linkedin': 'https://www.linkedin.com/in/aaronreidsmith',
            'github': 'https://github.com/aaronreidsmith',
            'stack_overflow': 'https://stackoverflow.com/users/10696164/aaron-smith'
        }
        self.skills = {
            'languages': ['Python', 'SQL', 'Scala', 'Java', 'Bash', 'R', 'Perl', 'PHP'],
            'big_data': ['Spark', 'Databricks', 'Kinesis', 'Kafka', 'Hadoop'],
            'databases': ['Snowflake', 'Redshift', 'MySQL', 'PostgreSQL', 'DynamoDB'],
            'ci_cd': ['Azure Pipelines', 'GitHub Actions', 'Jenkins', 'Travis CI', 'Appveyor', 'CircleCI'],
            'cloud_platforms': ['Amazon Web Services', 'Google Cloud Platform']
        }
        
    def __str__(self):
        return f"Hi, I'm {self.name}. Nice to meet you!"


me = AaronReidSmith()    
print(me)
# Hi, I'm Aaron Smith. Nice to meet you!
```

</p>
</details>

<details><summary>Scala</summary>
<p>

```scala
class AaronReidSmith {
  val userName: String = "aaronreidsmith"
  val name: String     = "Aaron Smith"
  val email: String    = "aaronreidsmith@gmail.com"
  val social: Map[String, String] = Map(
    "linkedin"      -> "https://www.linkedin.com/in/aaronreidsmith",
    "github"        -> "https://github.com/aaronreidsmith",
    "stackOverflow" -> "https://stackoverflow.com/users/10696164/aaron-smith"
  )
  val skills: Map[String, Seq[String]] = Map(
    "languages"      -> Seq("Python", "SQL", "Scala", "Java", "Bash", "R", "Perl", "PHP"),
    "bigData"        -> Seq("Spark", "Databricks", "Kinesis", "Kafka", "Hadoop"),
    "databases"      -> Seq("Snowflake", "Redshift", "MySQL", "PostgreSQL", "DynamoDB"),
    "ciCd"           -> Seq("Azure Pipelines", "GitHub Actions", "Jenkins", "Travis CI", "Appveyor", "CircleCI"),
    "cloudPlatforms" -> Seq("Amazon Web Services", "Google Cloud Platform")
  )

  override def toString: String = s"Hi, I'm $name. Nice to meet you!"
}

val me = new AaronReidSmith
println(me)
// Hi, I'm Aaron Smith. Nice to meet you!
```

</p>
</details>

<details><summary>SQL (PostgreSQL)</summary>
<p>

```sql
CREATE TABLE aaron_reid_smith(
  username VARCHAR,
  name     VARCHAR,
  email    VARCHAR,
  social   JSON,
  skills   JSON
);

INSERT INTO aaron_reid_smith VALUES (
  'aaronreidsmith',
  'Aaron Smith',
  'aaronreidsmith@gmail.com',
  $$
  {
    "linkedin": "https://www.linkedin.com/in/aaronreidsmith",
    "github": "https://github.com/aaronreidsmith",
    "stack_overflow": "https://stackoverflow.com/users/10696164/aaron-smith"
  }
  $$,
  $$
  {
    "languages": ["Python", "SQL", "Scala", "Java", "Bash", "R", "Perl", "PHP"],
    "big_data": ["Spark", "Databricks", "Kinesis", "Kafka", "Hadoop"],
    "databases": ["Snowflake", "Redshift", "MySQL", "PostgreSQL", "DynamoDB"],
    "ci_cd": ["Azure Pipelines", "GitHub Actions", "Jenkins", "Travis CI", "Appveyor", "CircleCI"],
    "cloud_platforms": ["Amazon Web Services", "Google Cloud Platform"]
  }
  $$
);

SELECT
  $$Hi, I'm $$ || name || $$. Nice to meet you!$$
FROM aaron_reid_smith
-- Hi, I'm Aaron Smith. Nice to meet you!
```

</p>
</details>
