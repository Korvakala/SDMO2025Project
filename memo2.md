Koodin ajaminen käsin:

    repo_url = "https://github.com/EbookFoundation/free-programming-books"
    csv_path = "project1devs"
    csv_name = "devs.csv"
    output_path = "results"
    similarity_threshold = 0.9

import kaikki paketit

DEVS = set()
for commit in Repository(repo_url).traverse_commits():
    DEVS.add((commit.author.name, commit.author.email))
    DEVS.add((commit.committer.name, commit.committer.email))

-- output:
('Nathan Jones', 'nathan.jones@ironmail.org')
('Michael Obi', 'o.michael@binghamuni.edu.ng')
('dimasgt', '49423419+candraw@users.noreply.github.com')
...

DEVS = sorted(DEVS)

- param: path = csv_path, file_name = csv_name

with open(os.path.join(path, file_name), 'w', encoding=default_encoding, newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"')
    writer.writerow(["name", "email"])
    writer.writerows(DEVS)

-- output: kirjoitti devs.csv:n oikeaan kansioon

main -- devs = read_devs(csv_path, csv_name)

DEVS = []
with open(os.path.join(path, file_name), 'r', encoding=default_encoding, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        DEVS.append(row)
-- output:
[['name', 'email'], ['-=fAlC0n=-', 'Falcon@ssm3807.student.rit.edu'], ['-_-', '117875736+Keerthan04@users.noreply.github.com']]

# First element is header, skip
DEVS = DEVS[1:]
main -- devs = DEVS
main -- similarity_data = compute_similarity(devs)

# Dataa vähemmäksi
devs = devs[:3]
- output:
[['-=fAlC0n=-', 'Falcon@ssm3807.student.rit.edu'], ['-_-', '117875736+Keerthan04@users.noreply.github.com'], ['0xCD', '0xCD@users.noreply.github.com']]

compute_similarity(devs)
SIMILARITY = []
for dev_a, dev_b in combinations(developers, 2):
    # Pre-process both developers
    name_a, first_a, last_a, i_first_a, i_last_a, email_a, prefix_a = preprocess(dev_a)
    name_b, first_b, last_b, i_first_b, i_last_b, email_b, prefix_b = preprocess(dev_b)
    
# skip for loop: yksittäiset esimerkit
>>> dev_a, dev_b = list(combinations(devs, 2))[0]
>>> dev_a
['-=fAlC0n=-', 'Falcon@ssm3807.student.rit.edu']
>>> dev_b
['-_-', '117875736+Keerthan04@users.noreply.github.com']

# preprocessing
>>> name: str = dev_a[0]
>>> name
'-=fAlC0n=-'

    # Conditions of Bird heuristic
    c1 = sim(name_a, name_b)
    c2 = sim(prefix_b, prefix_a)
    c31 = sim(first_a, first_b)
    c32 = sim(last_a, last_b)
    c4 = c5 = c6 = c7 = False
    # Since lastname and initials can be empty, perform appropriate checks
    if i_first_a != "" and last_a != "":
        c4 = i_first_a in prefix_b and last_a in prefix_b
    if i_last_a != "":
        c5 = i_last_a in prefix_b and first_a in prefix_b
    if i_first_b != "" and last_b != "":
        c6 = i_first_b in prefix_a and last_b in prefix_a
    if i_last_b != "":
        c7 = i_last_b in prefix_a and first_b in prefix_a

    # Save similarity data for each conditions. Original names are saved
    SIMILARITY.append([dev_a[0], email_a, dev_b[0], email_b, c1, c2, c31, c32, c4, c5, c6, c7])

