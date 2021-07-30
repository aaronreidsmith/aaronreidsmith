# Hi There 👋
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/aaronreidsmith/)](https://www.linkedin.com/in/aaronreidsmith/)
[![Stack Overflow](https://img.shields.io/badge/-Stack_Overflow-FE7A16?style=flat&logo=Stack-Overflow&logoColor=white&link=https://stackoverflow.com/users/10696164/aaron-smith)](https://stackoverflow.com/users/10696164/aaron-smith)
[![Gmail](https://img.shields.io/badge/-Email-D14836?style=flat&logo=Gmail&logoColor=white&link=mailto:aaronreidsmith@gmail.com)](mailto:aaronreidsmith@gmail.com)

## About me
I'm Aaron Smith, a Senior Data Engineer at [IronNet Cybersecurity](https://www.ironnet.com/) and an active contributor to Python's leading equivalent to R's `auto.arima`, [`pmdarima`](https://github.com/alkaline-ml/pmdarima). Currently working to process billions of data points per day using Scala and Spark.

Feel free to contact me through my social links above, give my [blog](https://aaronreidsmith.github.io) a read, or take a look at my summary-as-code (in your preferred language) below!


## Summary-as-Code

<details open><summary>Scala</summary>
<p>

```scala
case class Person(
  username: String,
  name: String,
  email: String,
  social: Map[String, String],
  skills: Map[String, Seq[String]]
) {
  override def toString: String = s"Hi, I'm $name. Nice to meet you!"
}

val me = Person(
  username = "aaronreidsmith",
  name     = "Aaron Smith",
  email    = "aaronreidsmith@gmail.com",
  social = Map(
    "linkedin"      -> "https://www.linkedin.com/in/aaronreidsmith/",
    "github"        -> "https://github.com/aaronreidsmith",
    "stackOverflow" -> "https://stackoverflow.com/users/10696164/aaron-smith"
  ),
  skills = Map(
    "languages"      -> Seq("Scala", "Python", "SQL", "Java", "Bash", "Raku", "R", "Perl", "PHP"),
    "bigData"        -> Seq("Kafka", "Spark", "Databricks", "Kinesis", "Hadoop", "HBase", "Zookeeper", "Hive", "Pig"),
    "databases"      -> Seq("Snowflake", "Redshift", "MySQL", "PostgreSQL", "DynamoDB"),
    "ciCd"           -> Seq("Azure Pipelines", "GitHub Actions", "Jenkins", "Travis CI", "Appveyor", "CircleCI"),
    "cloudPlatforms" -> Seq("Amazon Web Services", "Google Cloud Platform")
  )
)
println(me)
// Hi, I'm Aaron Smith. Nice to meet you!
```

</p>
</details>

<details><summary>Python</summary>
<p>

```python
from __future__ import annotations  # Needed for versions <3.9
from dataclasses import dataclass


@dataclass
class Person:
    username: str
    name: str
    email: str
    social: dict[str, str]
    skills: dict[str, list[str]]
    
    def __str__(self) -> str:
        return f"Hi, I'm {self.name}. Nice to meet you!"
		
me = Person(
    username = 'aaronreidsmith',
    name = 'Aaron Smith',
    email = 'aaronreidsmith@gmail.com',
    social = {
        'linkedin': 'https://www.linkedin.com/in/aaronreidsmith/',
        'github': 'https://github.com/aaronreidsmith',
        'stack_overflow': 'https://stackoverflow.com/users/10696164/aaron-smith'
    },
    skills = {
        'languages': ['Scala', 'Python', 'SQL', 'Java', 'Bash', 'Raku', 'R', 'Perl', 'PHP'],
        'big_data': ['Kafka', 'Spark', 'Databricks', 'Kinesis', 'Hadoop', 'Zookeeper', 'Hive', 'Pig'],
        'databases': ['Snowflake', 'Redshift', 'MySQL', 'PostgreSQL', 'DynamoDB'],
        'ci_cd': ['Azure Pipelines', 'GitHub Actions', 'Jenkins', 'Travis CI', 'Appveyor', 'CircleCI'],
        'cloud_platforms': ['Amazon Web Services', 'Google Cloud Platform']
    }
)
print(me)
# Hi, I'm Aaron Smith. Nice to meet you!
```

</p>
</details>

<details><summary>SQL (PostgreSQL)</summary>
<p>

```sql
CREATE TABLE people (
  username VARCHAR PRIMARY KEY,
  name     VARCHAR,
  email    VARCHAR,
  social   JSON,
  skills   JSON
);

INSERT INTO people VALUES (
  'aaronreidsmith',
  'Aaron Smith',
  'aaronreidsmith@gmail.com',
  $$
  {
    "linkedin": "https://www.linkedin.com/in/aaronreidsmith/",
    "github": "https://github.com/aaronreidsmith",
    "stack_overflow": "https://stackoverflow.com/users/10696164/aaron-smith"
  }
  $$,
  $$
  {
    "languages": ["Scala", "Python", "SQL", "Java", "Bash", "Raku", "R", "Perl", "PHP"],
    "big_data": ["Kafka", "Spark", "Databricks", "Kinesis", "Hadoop", "HBase", "Zookeeper", "Hive", "Pig"],
    "databases": ["Snowflake", "Redshift", "MySQL", "PostgreSQL", "DynamoDB"],
    "ci_cd": ["Azure Pipelines", "GitHub Actions", "Jenkins", "Travis CI", "Appveyor", "CircleCI"],
    "cloud_platforms": ["Amazon Web Services", "Google Cloud Platform"]
  }
  $$
);

SELECT
  'Hi, I''m ' || name || '. Nice to meet you!' AS me
FROM people
WHERE username = 'aaronreidsmith';
-- Hi, I'm Aaron Smith. Nice to meet you!
```

</p>
</details>

<details closed><summary>Raku</summary>
<p>

```raku
class Person {
    has Str  $.username;
    has Str  $.name;
    has Str  $.email;
    has Str  %.social{Str};
    has List %.skills{Str};

    method gist returns Str {
        "Hi, I'm $!name. Nice to meet you!";
    }
}

my $me = Person.new(
    username => 'aaronreidsmith',
    name     => 'Aaron Smith',
    email    => 'aaronreidsmith@gmail.com',
    social => (
        'linkedin'       => 'https://www.linkedin.com/in/aaronreidsmith/',
        'github'         => 'https://github.com/aaronreidsmith',
        'stack-overflow' => 'https://stackoverflow.com/users/10696164/aaron-smith'
    ),
    skills => (
        'languages'       => ('Scala', 'Python', 'SQL', 'Java', 'Bash', 'Raku', 'R', 'Perl', 'PHP'),
        'big-data'        => ('Kafka', 'Spark', 'Databricks', 'Kinesis', 'Hadoop', 'Zookeeper', 'Hive', 'Pig'),
        'databases'       => ('Snowflake', 'Redshift', 'MySQL', 'PostgreSQL', 'DynamoDB'),
        'ci-cd'           => ('Azure Pipelines', 'GitHub Actions', 'Jenkins', 'Travis CI', 'Appveyor', 'CircleCI'),
        'cloud-platforms' => ('Amazon Web Services', 'Google Cloud Platform')
    )
);
say $me;
# Hi, I'm Aaron Smith. Nice to meet you!
```

</p>
</details>

<details closed><summary>PHP</summary>
<p>

```php
<?php
class Person {
    public $username;
    public $name;
    public $email;
    public $social;
    public $skills;

    public function __construct($username, $name, $email, $social, $skills) {
        $this->username = $username;
        $this->name     = $name;
        $this->email    = $email;
        $this->social   = $social;
        $this->skills   = $skills;
    }

    public function __toString() {
        return "Hi, I'm {$this->name}. Nice to meet you!\n";
    }
}

$me = new Person(
    'aaronreidsmith',
    'Aaron Smith',
    'aaronreidsmith@gmail.com',
    array(
        'linkedin'       => 'https://www.linkedin.com/in/aaronreidsmith/',
        'github'         => 'https://github.com/aaronreidsmith',
        'stack_overflow' => 'https://stackoverflow.com/users/10696164/aaron-smith'
    ),
    array(
        'languages'       => array('Scala', 'Python', 'SQL', 'Java', 'Bash', 'Raku', 'R', 'Perl', 'PHP'),
        'big_data'        => array('Kafka', 'Spark', 'Databricks', 'Kinesis', 'Hadoop', 'Zookeeper', 'Hive', 'Pig'),
        'databases'       => array('Snowflake', 'Redshift', 'MySQL', 'PostgreSQL', 'DynamoDB'),
        'ci_cd'           => array('Azure Pipelines', 'GitHub Actions', 'Jenkins', 'Travis CI', 'Appveyor', 'CircleCI'),
        'cloud_platforms' => array('Amazon Web Services', 'Google Cloud Platform')
    )
);
echo $me;
# Hi, I'm Aaron Smith. Nice to meet you!
```

</p>
</details>

