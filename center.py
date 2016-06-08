import media
import fresh_tomatoes

#creating movie objects 
toy_story = media.Movie("Toy Story", 
						"""In a world
where toys pretend to be lifeless in the presence of humans, Woody, a
pullstring cowboy doll, is the leader of a group of toys that are owned by a
boy named Andy Davis. With his family moving away one week before his
birthday, Andy is given a week-early party to spend with his friends, while
the toys stage a reconnaissance mission to discover Andy's new presents. Andy
receives a spaceman action figure named Buzz Lightyear, whose impressive
features see him replacing Woody as Andy's favorite toy. Woody becomes
jealous, especially when he notices that Buzz also gets attention from the
other toys. However, Buzz thinks he is a real space ranger on a mission to
return to his home planet, while Woody tries to convince him that he is just a
toy.""" , 
					"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",   #noqa
					"https://www.youtube.com/watch?v=KYz2wyBy3kc") 
deadpool = media.Movie("Deadpool", 
				"""Wade Wilson is a former special forces operative who
works as a mercenary in New York City. He meets escort Vanessa Carlysle at a
local bar and they become romantically attached. One year later, Wade proposes
to marry her and she accepts, but he suddenly collapses. Wade is diagnosed
with terminal cancer, and though Vanessa remains by his side, he does not want
her to watch him die.""",
					"https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",  #noqa
					"https://www.youtube.com/watch?v=gtTfd6tISfw") 
furious_7 = media.Movie("Furious 7", 
				"""After defeating Owen Shaw and his crew and securing
amnesty for their past crimes, Dominic Dom Toretto, Brian O'Conner, and the
rest of their team have returned to the United States to live normal lives
again. Brian begins to accustom himself to life as a father, while Dom tries
to help Letty Ortiz regain her memories. Meanwhile, Owen's older brother,
Deckard Shaw, breaks into the secure hospital the comatose Owen is being held
in and swears vengeance against Dom, before breaking into Luke Hobbs' DSS
office to extract profiles of Dom's crew. After revealing his identity, Shaw
engages Hobbs in a fight, and escapes when he detonates a bomb that severely
injures Hobbs. Dom later learns from his sister Mia that she is pregnant again
and convinces her to tell Brian. However, a bomb, disguised in a package sent
from Tokyo, explodes and destroys the Toretto house just seconds after Han, a
member of their team, is killed by Shaw in Tokyo. Dom later visits Hobbs in a
hospital, where he learns that Shaw is a rogue special forces assassin seeking
to avenge his brother. Dom then travels to Tokyo to claim Han's body, and
meets and races Sean Boswell, a friend of Han's who gives him personal items
found at Han's crash site. At Han's funeral in Los Angeles, Dom notices a car
observing them, and after a chase, confronts its driver, Shaw. Both prepare to
fight, Shaw slips away when a covert ops team arrives and opens fire. The team
is led by a man who calls himself Mr. Nobody, who says that he will assist Dom
in stopping Shaw if he helps him obtain the God's Eye, a computer program that
uses digital devices to track down a person, and save its creator, a hacker
named Ramsey, from a mercenary named Mose Jakande. Dom, Brian, Letty, Roman
Pearce, and Tej Parker then airdrop their cars over the Caucasus Mountains in
Azerbaijan, ambush Jakande's convoy, and rescue Ramsey. The team then heads to
Abu Dhabi, where a billionaire has acquired the flash drive containing the
God's Eye, and manages to steal it from the owner. With the God's Eye near
telecommunications repeaters, the team tracks down Shaw, who is waiting at a
remote factory. Dom, Brian, Mr. Nobody and his team attempt to capture Shaw,
but are ambushed by Jakande and his team, and are forced to flee while Jakande
obtains the God's Eye. At his own request, Mr. Nobody is then left to be
evacuated by helicopter. Left with no other choice, the team returns to Los
Angeles to fight Shaw, Jakande and his men. Meanwhile, Brian promises Mia that
once they deal with Shaw, he will dedicate himself entirely to their family.
While Jakande pursues Brian and the rest of the team with a stealth helicopter
and an aerial drone, Ramsey attempts to hack into the God's Eye. Hobbs, seeing
the team in trouble, leaves the hospital and destroys the drone with an
ambulance. Ramsey then regains control of the God's Eye and shuts it down.
Meanwhile, Dom and Shaw engage in a one-on-one brawl on a parking garage,
before Jakande intervenes and attacks them both. Shaw is defeated when part of
the parking garage collapses beneath him. Dom then launches his vehicle at
Jakande's helicopter, tossing Shaw's bag of grenades onto its skids, before
injuring himself when his car lands and crashes. Hobbs then shoots the bag of
grenades from ground level, destroying the helicopter and killing Jakande. Dom
is pulled from the wreckage of his car, believed dead. As Letty cradles Dom's
body in her arms, she reveals that she has regained her memories, and that she
remembers their wedding. Dom regains consciousness soon after, remarking, It's
about time. Shaw is taken into custody by Hobbs and locked away in a secret,
high-security prison, 32 meters underground. At a beach, Brian and Mia play
with their son while Dom, Letty, Roman, Tej and Ramsey observe, acknowledging
that Brian is better off retired with his family. Dom silently leaves, but
Brian catches up with him at a crossroad. As Dom remembers the times that he
had with Brian, they bid each other farewell and drive off in separate
directions.""",
					"https://upload.wikimedia.org/wikipedia/en/b/b8/Furious_7_poster.jpg",  #noqa
					"https://www.youtube.com/watch?v=Skpu5HaVkOc") 
warcraft = media.Movie("Warcraft", 
				"""Looking to escape from his dying world, the orc
shaman Gul'dan utilizes dark magic to open a portal to the human realm of
Azeroth. Supported by the fierce fighter Blackhand, Gul'dan organizes the orc
clans into a conquering army called the Horde. Uniting to protect Azeroth from
these hulking invaders are King Llane, the mighty warrior Anduin Lothar
(Travis Fimmel) and the powerful wizard Medivh. As the two races collide,
leaders from each side start to question if war is the only answer.""",
 						"https://upload.wikimedia.org/wikipedia/en/thumb/5/56/Warcraft_Teaser_Poster.jpg/440px-Warcraft_Teaser_Poster.jpg",  #noqa
						"https://www.youtube.com/watch?v=RhFMIRuHAL4") 
civil_war = media.Movie("Captain America: Civil War", 
				"""Political pressure mounts to
install a system of accountability when the actions of the Avengers lead to
collateral damage. The new status quo deeply divides members of the team.
Captain America (Chris Evans) believes superheroes should remain free to
defend humanity without government interference. Iron Man (Robert Downey Jr.)
sharply disagrees and supports oversight. As the debate escalates into an all-
out feud, Black Widow (Scarlett Johansson) and Hawkeye (Jeremy Renner) must
pick a side.""", 
						"https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",  #noqa
						"https://www.youtube.com/watch?v=dKrVegVI0Us") 
spectre = media.Movie("Spectre", 
			"""A cryptic message from the past leads James Bond
(Daniel Craig) to Mexico City and Rome, where he meets the beautiful widow
(Monica Bellucci) of an infamous criminal. After infiltrating a secret
meeting, 007 uncovers the existence of the sinister organization SPECTRE.
Needing the help of the daughter of an old nemesis, he embarks on a mission to
find her. As Bond ventures toward the heart of SPECTRE, he discovers a
chilling connection between himself and the enemy (Christoph Waltz) he
seeks.""", 
						"https://upload.wikimedia.org/wikipedia/en/c/c3/Spectre_poster.jpg",  #noqa
						"https://www.youtube.com/watch?v=z4UDNzXD3qA")

#adding movie objects to a list
movies = [toy_story, deadpool, furious_7, warcraft, civil_war, spectre]
fresh_tomatoes.open_movies_page(movies)
