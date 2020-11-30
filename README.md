# Hi There 👋
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?style=flat&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/aaronreidsmith/)](https://www.linkedin.com/in/aaronreidsmith/)
[![Stack Overflow](https://img.shields.io/badge/-Stack_Overflow-FE7A16?style=flat&logo=Stack-Overflow&logoColor=white&link=https://stackoverflow.com/users/10696164/aaron-smith)](https://stackoverflow.com/users/10696164/aaron-smith)
[![Gmail](https://img.shields.io/badge/-Email-D14836?style=flat&logo=Gmail&logoColor=white&link=mailto:aaronreidsmith@gmail.com)](mailto:aaronreidsmith@gmail.com)

## About me
I'm Aaron Smith, a Data Engineer at [Sumo Logic](https://www.sumologic.com/) and an active contributor to Python's leading equivalent to R's `auto.arima`, [`pmdarima`](https://github.com/alkaline-ml/pmdarima). Currently working to process billions of data points per day using Scala and Kafka Streams.

Feel free to contact me through my social links above, and take a look at my summary-as-code (in your preferred language) below!


## Summary-as-Code 

<details open><summary>Python</summary>
<p>

```python
from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Person:
    username: str
    name: str
    email: str
    social: Dict[str, str]
    skills: Dict[str, List[str]]
    
    def __str__(self):
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
        'languages': ['Python', 'SQL', 'Scala', 'Java', 'Bash', 'Raku', 'R', 'Perl', 'PHP'],
        'big_data': ['Spark', 'Databricks', 'Kinesis', 'Kafka', 'Hadoop'],
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

<details><summary>Scala</summary>
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
  social   = Map(
    "linkedin"      -> "https://www.linkedin.com/in/aaronreidsmith/",
    "github"        -> "https://github.com/aaronreidsmith",
    "stackOverflow" -> "https://stackoverflow.com/users/10696164/aaron-smith"
  ),
  skills = Map(
    "languages"      -> Seq("Python", "SQL", "Scala", "Java", "Bash", "Raku", "R", "Perl", "PHP"),
    "bigData"        -> Seq("Spark", "Databricks", "Kinesis", "Kafka", "Hadoop"),
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
    "languages": ["Python", "SQL", "Scala", "Java", "Bash", "Raku", "R", "Perl", "PHP"],
    "big_data": ["Spark", "Databricks", "Kinesis", "Kafka", "Hadoop"],
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
    social   => (
        'linkedin'       => 'https://www.linkedin.com/in/aaronreidsmith/',
        'github'         => 'https://github.com/aaronreidsmith',
        'stack-overflow' => 'https://stackoverflow.com/users/10696164/aaron-smith'
    ),
    skills => (
        'languages'       => ('Python', 'SQL', 'Scala', 'Java', 'Bash', 'Raku', 'R', 'Perl', 'PHP'),
        'big-data'        => ('Spark', 'Databricks', 'Kinesis', 'Kafka', 'Hadoop'),
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
        'languages'       => array('Python', 'SQL', 'Scala', 'Java', 'Bash', 'Raku', 'R', 'Perl', 'PHP'),
        'big_data'        => array('Spark', 'Databricks', 'Kinesis', 'Kafka', 'Hadoop'),
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

