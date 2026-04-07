|     |     |     |     | Programming |     |     | as    | Theory |     | Building |     |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | ----- | ------ | --- | -------- | --- | --- | --- | --- |
|     |     |     |     |             |     |     | Peter | Naur   |     |          |     |     |     |     |
1985
Peter Naur’s classic 1985 essay “Programming as Theory Building” argues that a program
is not its source code. A program is a shared mental construct (he uses the word theory)
that lives in the minds of the people who work on it. If you lose the people, you lose the
program. Thecodeismerelyawrittenrepresentationoftheprogram,andit’slossy,soyou
can’treconstructaprogramfromitscode.
Introduction in the real world activity being matched by the program
|             |            |     |     |                |     |        |        | execution, | in  | other words | program | modifications. |     |     |
| ----------- | ---------- | --- | --- | -------------- | --- | ------ | ------ | ---------- | --- | ----------- | ------- | -------------- | --- | --- |
| The present | discussion |     | is  | a contribution |     | to the | under- |            |     |             |         |                |     |     |
standing of what programming is. It suggests that pro- One way of stating the main point I want to make
| gramming | properly |     | should | be regarded |     | as an activity | by  |         |             |     |            |           |      |        |
| -------- | -------- | --- | ------ | ----------- | --- | -------------- | --- | ------- | ----------- | --- | ---------- | --------- | ---- | ------ |
|          |          |     |        |             |     |                |     | is that | programming | in  | this sense | primarily | must | be the |
whichtheprogrammersformorachieveacertainkindof programmers’ building up knowledge of a certain kind,
insight, a theory, of the matters at hand. This sugges- knowledgetakentobebasicallytheprogrammers’imme-
tionisincontrasttowhatappearstobeamorecommon
|     |     |     |     |     |     |     |     | diate possession, |     | any | documentation |     | being an | auxiliary, |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | ------------- | --- | -------- | ---------- |
notion, that programming should be regarded as a pro- secondary product.
| duction | of a program |     | and | certain | other | texts. |     |     |              |     |        |         |             |         |
| ------- | ------------ | --- | --- | ------- | ----- | ------ | --- | --- | ------------ | --- | ------ | ------- | ----------- | ------- |
|         |              |     |     |         |       |        |     | As  | a background |     | of the | further | elaboration | of this |
Someofthebackgroundoftheviewspresentedhereis
viewgiveninthefollowingsections,theremainderofthe
tobefoundincertainobservationsofwhatactuallyhap-
presentsectionwilldescribesomerealexperienceofdeal-
| pens to | programs | and | the | teams of | programmers |     | dealing |     |     |     |     |     |     |     |
| ------- | -------- | --- | --- | -------- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
ingwithlargeprogramsthathasseemedtomemoreand
| with them, | particularly |     | in  | situations | arising | from | unex- |                  |     |      |               |     |          |           |
| ---------- | ------------ | --- | --- | ---------- | ------- | ---- | ----- | ---------------- | --- | ---- | ------------- | --- | -------- | --------- |
|            |              |     |     |            |         |      |       | more significant |     | as I | have pondered |     | over the | problems. |
pected and perhaps erroneous program executions or re- Ineithercasetheexperienceismyownorhasbeencom-
actions,andontheoccasionofmodificationsofprograms.
|                |      |                  |     |     |                   |      |           | municated | to       | me by        | persons | having | first hand | contact |
| -------------- | ---- | ---------------- | --- | --- | ----------------- | ---- | --------- | --------- | -------- | ------------ | ------- | ------ | ---------- | ------- |
| The difficulty |      | of accommodating |     |     | such observations |      | in a      |           |          |              |         |        |            |         |
|                |      |                  |     |     |                   |      |           | with the  | activity | in question. |         |        |            |         |
| production     | view | of programming   |     |     | suggests          | that | this view |           |          |              |         |        |            |         |
is misleading. The theory building view is presented as Case 1 concerns a compiler. It has been developed
an alternative.
|        |         |     |            |     |                  |     |      | by a group | A   | for a Language                    |      | L and | worked very      | well on |
| ------ | ------- | --- | ---------- | --- | ---------------- | --- | ---- | ---------- | --- | --------------------------------- | ---- | ----- | ---------------- | ------- |
|        |         |     |            |     |                  |     |      | computerX. |     | NowanothergroupBhasthetasktowrite |      |       |                  |         |
| A more | general |     | background | of  | the presentation |     | is a |            |     |                                   |      |       |                  |         |
|        |         |     |            |     |                  |     |      | a compiler | for | a language                        | L+M, | a     | modest extension | of      |
convictionthatitisimportanttohaveanappropriateun-
|             |     |      |             |     |        |                 |     | L, for computer |     | Y. Group | B   | decides | that the | compiler |
| ----------- | --- | ---- | ----------- | --- | ------ | --------------- | --- | --------------- | --- | -------- | --- | ------- | -------- | -------- |
| derstanding | of  | what | programming |     | is. If | our understand- |     |                 |     |          |     |         |          |          |
forLdevelopedbygroupAwillbeagoodstartingpoint
ingisinappropriatewewillmisunderstandthedifficulties
|            |        |          |           |     |               |     |          | for their | design,   | and     | get a contract |         | with group          | A that     |
| ---------- | ------ | -------- | --------- | --- | ------------- | --- | -------- | --------- | --------- | ------- | -------------- | ------- | ------------------- | ---------- |
| that arise | in the | activity | and       | our | attempts      | to  | overcome |           |           |         |                |         |                     |            |
|            |        |          |           |     |               |     |          | they will | get       | support | in the         | form of | full documentation, |            |
| them will  | give   | rise to  | conflicts | and | frustrations. |     |          |           |           |         |                |         |                     |            |
|            |        |          |           |     |               |     |          | including | annotated | program |                | texts   | and much            | additional |
In the present discussion some of the crucial back- written design discussion, and also personal advice. The
ground experience will first be outlined. This is followed arrangement was effective and group B managed to de-
by an explanation of a theory of what programming is, velop the compiler they wanted. In the present context
denoted the Theory Building View. The subsequent sec- thesignificantissueistheimportanceofthepersonalad-
tions enter into some of the consequences of the Theory vice from group A in the matters that concerned how to
Building View. implementtheextensionsM tothelanguage. Duringthe
|             |     |         |              |     |           |     |     | design    | phase | group B    | made   | suggestions | for the      | manner |
| ----------- | --- | ------- | ------------ | --- | --------- | --- | --- | --------- | ----- | ---------- | ------ | ----------- | ------------ | ------ |
|             |     |         |              |     |           |     |     | in which  | the   | extensions | should | be          | accommodated | and    |
| Programming |     | and the | Programmers’ |     | Knowledge |     |     |           |       |            |        |             |              |        |
|             |     |         |              |     |           |     |     | submitted | them  | to group   | A for  | review.     | In several   | major  |
Ishallusethewordprogrammingtodenotethewholeac- casesitturnedoutthatthesolutionssuggestedbygroup
tivity of design and implementation of programmed so- B were found by group A to make no use of the facili-
lutions. What I am concerned with is the activity of ties that were not only inherent in the structure of the
matching some significant part and aspect of an activity existingcompilerbutwerediscussedatlengthinitsdoc-
intherealworldtotheformalsymbolmanipulationthat umentation,andtobebasedinsteadonadditionstothat
can be done by a program running on a computer. With structureintheformofpatchesthateffectivelydestroyed
such a notion it follows directly that the programming its power and simplicity. The members of group A were
activity I am talking about must include the develop- abletospotthesecasesinstantlyandcouldproposesim-
ment in time corresponding to the changes taking place pleandeffectivesolutions,framedentirelywithintheex-
1

isting structure. This is an example of how the full pro- briefly, a person who has or possesses a theory in this
gram text and additional documentation is insufficient sense knows how to do certain things and in addition
in conveying to even the highly motivated group B the can support the actual doing with explanations, justi-
deeper insight into the design, that theory which is im- fications, and answers to queries, about the activity of
mediately present to the members of group A. concern. It may be noted that Ryle’s notion of the-
ory appears as an example of what K. Popper [10] calls
Intheyearsfollowingtheseeventsthecompilerdevel-
unembodied World 3 objects and thus has a defensible
oped by group B was taken over by other programmers
philosophical standing. In the present section we shall
of the same organization, without guidance from group
describe Ryle’s notion of theory in more detail.
A. Information obtained by a member of group A about
thecompilerresultingfromthefurthermodificationofit Ryle [11] develops his notion of theory as part of his
afterabout10yearsmadeitclearthatatthatlaterstage analysisofthenatureofintellectualactivity,particularly
theoriginalpowerfulstructurewasstillvisible,butmade themannerinwhichintellectualactivitydiffersfrom,and
entirely ineffective by amorphous additions of many dif- goes beyond, activity that is merely intelligent. In intel-
ferent kinds. Thus, again, the program text and its doc- ligent behaviour the person displays, not any particular
umentationhasprovedinsufficientasacarrierofsomeof knowledge of facts, but the ability to do certain things,
the most important design ideas. such as to make and appreciate jokes, to talk grammat-
ically, or to fish. More particularly, the intelligent per-
Case2concernstheinstallationandfaultdiagnosisof
formance is characterized in part by the person’s doing
a large real–time system for monitoring industrial pro-
them well, according to certain criteria, but further dis-
duction activities. The system is marketed by its pro-
plays the person’s ability to apply the criteria so as to
ducer, each delivery of the system being adapted indi-
detect and correct lapses, to learn from the examples
vidually to its specific environment of sensors and dis-
of others, and so forth. It may be noted that this no-
play devices. The size of the program delivered in each
tion of intelligence does not rely on any notion that the
installation is of the order of 200,000 lines. The relevant
intelligent behaviour depends on the person’s following
experience from the way this kind of system is handled
or adhering to rules, prescriptions, or methods. On the
concerns the role and manner of work of the group of in-
contrary, the very act of adhering to rules can be done
stallation and fault finding programmers. The facts are,
more or less intelligently; if the exercise of intelligence
firstthattheseprogrammershavebeencloselyconcerned
dependedonfollowingrulestherewouldhavetoberules
with the system as a full time occupation over a period
about how to follow rules, and about how to follow the
of several years, from the time the system was under
rules about following rules, etc. in an infinite regress,
design. Second, when diagnosing a fault these program-
which is absurd.
mers rely almost exclusively on their ready knowledge of
the system and the annotated program text, and are un- What characterizes intellectual activity, over and be-
abletoconceiveofanykindofadditionaldocumentation yond activity that is merely intelligent, is the person’s
that would be useful to them. Third, other program- buildingandhavingatheory,wheretheoryisunderstood
mers’ groups who are responsible for the operation of astheknowledgeapersonmusthaveinordernotonlyto
particular installations of the system, and thus receive do certain things intelligently but also to explain them,
documentationofthesystemandfullguidanceonitsuse to answer queries about them, to argue about them, and
from the producer’s staff, regularly encounter difficulties so forth. A person who has a theory is prepared to enter
that upon consultation with the producer’s installation into such activities; while building the theory the person
and fault finding programmer are traced to inadequate is trying to get it.
understanding of the existing documentation, but which
canbeclearedupeasilybytheinstallationandfaultfind- Thenotionoftheoryinthesenseusedhereappliesnot
ing programmers. only to the elaborate constructions of specialized fields
of enquiry, but equally to activities that any person who
The conclusion seems inescapable that at least with
has received education will participate in on certain oc-
certain kinds of large programs, the continued adaption,
casions. Even quite unambitious activities of everyday
modification, and correction of errors in them, is essen-
life may give rise to people’s theorizing, for example in
tiallydependentonacertainkindofknowledgepossessed
planning how to place furniture or how to get to some
by a group of programmers who are closely and continu-
place by means of certain means of transportation.
ously connected with them.
The notion of theory employed here is explicitly not
confined to what may be called the most general or ab-
Ryle’s Notion of Theory
stract part of the insight. For example, to have New-
If it is granted that programming must involve, as the ton’s theory of mechanics as understood here it is not
essential part, a building up of the programmers’ knowl- enoughtounderstandthecentrallaws,suchasthatforce
edge, the next issue is to characterize that knowledge equalsmasstimesacceleration. Inaddition, asdescribed
moreclosely. Whatwillbeconsideredhereisthesugges- inmoredetailbyKuhn[4], thepersonhavingthetheory
tion that the programmers’ knowledge properly should must have an understanding of the manner in which the
be regarded as a theory, in the sense of Ryle [11]. Very central laws apply to certain aspects of reality, so as to
2

beabletorecognizeandapplythetheorytoothersimilar justificationisandmustalwaysremaintheprogrammer’s
aspects. A person having Newton’s theory of mechanics direct, intuitive knowledge or estimate. This holds even
must thus understand how it applies to the motions of where the justification makes use of reasoning, perhaps
pendulums and the planets, and must be able to recog- with application of design rules, quantitative estimates,
nize similar phenomena in the world, so as to be able to comparisons with alternatives, and such like, the point
employ the mathematically expressed rules of the theory being that the choice of the principles and rules, and the
properly. decision that they are relevant to the situation at hand,
|          |            |         |             |            |         |        |         | again must   | in  | the final         | analysis | remain | a   | matter | of the |
| -------- | ---------- | ------- | ----------- | ---------- | ------- | ------ | ------- | ------------ | --- | ----------------- | -------- | ------ | --- | ------ | ------ |
| The      | dependence |         | of a theory | on         | a grasp | of     | certain |              |     |                   |          |        |     |        |        |
|          |            |         |             |            |         |        |         | programmer’s |     | direct knowledge. |          |        |     |        |        |
| kinds of | similarity | between |             | situations | and     | events | of the  |              |     |                   |          |        |     |        |        |
real world gives the reason why the knowledge held by 3)Theprogrammerhavingthetheoryoftheprogram
someone who has the theory could not, in principle, be is able to respond constructively to any demand for a
expressed in terms of rules. In fact, the similarities in modification of the program so as to support the affairs
question are not, and cannot be, expressed in terms of of the world in a new manner. Designing how a modifi-
criteria,nomorethanthesimilaritiesofmanyotherkinds cation is best incorporated into an established program
| of objects, | such | as human | faces, | tunes, | or  | tastes | of wine, |         |        |            |     |                |     |        |     |
| ----------- | ---- | -------- | ------ | ------ | --- | ------ | -------- | ------- | ------ | ---------- | --- | -------------- | --- | ------ | --- |
|             |      |          |        |        |     |        |          | depends | on the | perception | of  | the similarity |     | of the | new |
can be thus expressed. demand with the operational facilities already built into
|     |     |     |     |     |     |     |     | the program. | The | kind | of similarity |     | that | has to | be per- |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---- | ------------- | --- | ---- | ------ | ------- |
The Theory To Be Built by the Programmer ceivedisonebetweenaspectsoftheworld. Itonlymakes
|          |           |        |     |         |      |        |          | sense to | the agent | who | has knowledge |     | of the | world, | that |
| -------- | --------- | ------ | --- | ------- | ---- | ------ | -------- | -------- | --------- | --- | ------------- | --- | ------ | ------ | ---- |
| In terms | of Ryle’s | notion | of  | theory, | what | has to | be built |          |           |     |               |     |        |        |      |
istotheprogrammer,andcannotbereducedtoanylim-
| by the | programmer | is  | a theory | of  | how certain | affairs | of  |     |     |     |     |     |     |     |     |
| ------ | ---------- | --- | -------- | --- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
itedsetofcriteriaorrules,forreasonssimilartotheones
the world will be handled by, or supported by, a com- given above why the justification of the program cannot
| puter program. |     | On     | the Theory | Building |             | View | of pro-  |         |          |     |     |     |     |     |     |
| -------------- | --- | ------ | ---------- | -------- | ----------- | ---- | -------- | ------- | -------- | --- | --- | --- | --- | --- | --- |
|                |     |        |            |          |             |      |          | be thus | reduced. |     |     |     |     |     |     |
| gramming       | the | theory | built      | by the   | programmers |      | has pri- |         |          |     |     |     |     |     |     |
macy over such other products as program texts, user While the discussion of the present section presents
documentation, and additional documentation such as some basic arguments for adopting the Theory Building
|     |     |     |     |     |     |     |     | View of | programming, |     | an assessment |     | of the | view | should |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ------------- | --- | ------ | ---- | ------ |
specifications.
|            |     |         |        |          |       |     |       | take into  | account       | to  | what extent | it          | may | contribute | to    |
| ---------- | --- | ------- | ------ | -------- | ----- | --- | ----- | ---------- | ------------- | --- | ----------- | ----------- | --- | ---------- | ----- |
| In arguing |     | for the | Theory | Building | View, | the | basic |            |               |     |             |             |     |            |       |
|            |     |         |        |          |       |     |       | a coherent | understanding |     | of          | programming |     | and its    | prob- |
issueistoshowhowtheknowledgepossessedbythepro-
|         |     |           |        |            |     |        |        | lems. Such | matters | will | be  | discussed | in  | the following |     |
| ------- | --- | --------- | ------ | ---------- | --- | ------ | ------ | ---------- | ------- | ---- | --- | --------- | --- | ------------- | --- |
| grammer | by  | virtue of | his or | her having | the | theory | neces- |            |         |      |     |           |     |               |     |
sections.
sarily,andinanessentialmanner,transcendsthatwhich
| is recorded | in  | the documented |     | products. | The | answers | to  |     |     |     |     |     |     |     |     |
| ----------- | --- | -------------- | --- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
thisissueisthattheprogrammer’sknowledgetranscends Problems and Costs of Program Modifications
thatgivenindocumentationinatleastthreeessentialar- A prominent reason for proposing the Theory Building
eas:
|     |     |     |     |     |     |     |     | View of    | programming |     | is the   | desire | to establish |     | an in- |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | -------- | ------ | ------------ | --- | ------ |
|     |     |     |     |     |     |     |     | sight into | programming |     | suitable | for    | supporting   | a   | sound  |
1)Theprogrammerhavingthetheoryoftheprogram
can explain how the solution relates to the affairs of the understanding of program modifications. This question
willthereforebethefirstonetobetakenupforanalysis.
| world that | it           | helps to | handle. | Such       | an explanation |       | will    |     |             |     |           |     |           |      |       |
| ---------- | ------------ | -------- | ------- | ---------- | -------------- | ----- | ------- | --- | ----------- | --- | --------- | --- | --------- | ---- | ----- |
| have to    | be concerned |          | with    | the manner | in             | which | the af- |     |             |     |           |     |           |      |       |
|            |              |          |         |            |                |       |         | One | thing seems | to  | be agreed | by  | everyone, | that | soft- |
fairsoftheworld,bothintheiroverallcharacteristicsand
|                  |        |             |            |             |                |             |          | ware will                       | be modified. |               | It is          | invariably | the            | case    | that a |
| ---------------- | ------ | ----------- | ---------- | ----------- | -------------- | ----------- | -------- | ------------------------------- | ------------ | ------------- | -------------- | ---------- | -------------- | ------- | ------ |
| their details,   |        | are, in     | some       | sense,      | mapped         | into the    | pro-     |                                 |              |               |                |            |                |         |        |
|                  |        |             |            |             |                |             |          | program,                        | once         | in operation, |                | will be    | felt to        | be only | part   |
| gram text        | and    | into any    | additional |             | documentation. |             | Thus     |                                 |              |               |                |            |                |         |        |
|                  |        |             |            |             |                |             |          | oftheanswertotheproblemsathand. |              |               |                |            | Alsotheveryuse |         |        |
| the programmer   |        | must        | be able    | to          | explain,       | for each    | part     |                                 |              |               |                |            |                |         |        |
|                  |        |             |            |             |                |             |          | of the program                  |              | itself will   | inspire        | ideas      | for            | further | useful |
| of the program   |        | text and    | for        | each of     | its overall    | structural  |          |                                 |              |               |                |            |                |         |        |
|                  |        |             |            |             |                |             |          | services                        | that the     | program       | ought          | to         | provide.       | Hence   | the    |
| characteristics, |        | what        | aspect     | or activity | of             | the         | world is |                                 |              |               |                |            |                |         |        |
|                  |        |             |            |             |                |             |          | need for                        | ways         | to handle     | modifications. |            |                |         |        |
| matched          | by it. | Conversely, |            | for any     | aspect         | or activity | of       |                                 |              |               |                |            |                |         |        |
the world the programmer is able to state its manner of The question of program modifications is closely tied
mapping into the program text. By far the largest part to that of programming costs. In the face of a need for a
of the world aspects and activities will of course lie out- changed manner of operation of the program, one hopes
side the scope of the program text, being irrelevant in toachieveasavingofcostsbymakingmodificationsofan
|              |          |                 |         |                    |            |        |         | existingprogramtext, |             |      | ratherthanbywritinganentirely |     |               |     |        |
| ------------ | -------- | --------------- | ------- | ------------------ | ---------- | ------ | ------- | -------------------- | ----------- | ---- | ----------------------------- | --- | ------------- | --- | ------ |
| the context. |          | However,        | the     | decision           | that       | a part | of the  |                      |             |      |                               |     |               |     |        |
| world is     | relevant | can             | only be | made               | by someone |        | who un- | new program.         |             |      |                               |     |               |     |        |
| derstands    | the      | whole world.    |         | This understanding |            |        | must be |                      |             |      |                               |     |               |     |        |
|              |          |                 |         |                    |            |        |         | The                  | expectation | that | program                       |     | modifications |     | at low |
| contributed  | by       | the programmer. |         |                    |            |        |         |                      |             |      |                               |     |               |     |        |
costoughttobepossibleisonethatcallsforcloseranaly-
2)Theprogrammerhavingthetheoryoftheprogram sis. Firstitshouldbenotedthatsuchanexpectationcan-
can explain why each part of the program is what it is, not be supported by analogy with modifications of other
inotherwordsisabletosupporttheactualprogramtext complicated man–made constructions. Where modifica-
with a justification of some sort. The final basis of the tions are occasionally put into action, for example in the
3

caseofbuildings,theyarewellknowntobeexpensiveand Inacertainsensetherecanbenoquestionofatheory
in fact complete demolition of the existing building fol- modification, only of a program modification. Indeed,
lowedbynewconstructionisoftenfoundtobepreferable a person having the theory must already be prepared
economically. Second, the expectation of the possibility to respond to the kinds of questions and demands that
of low cost program modifications conceivably finds sup- maygiverisetoprogrammodifications. Thisobservation
portinthefactthataprogramisatextheldinamedium leads to the important conclusion that the problems of
allowing for easy editing. For this support to be valid it program modification arise from acting on the assump-
must clearly be assumed that the dominating cost is one tion that programming consists of program text produc-
of text manipulation. This would agree with a notion of tion, instead of recognizing programming as an activity
programming as text production. On the Theory Build- of theory building.
| ingViewthiswholeargumentisfalse. |     |     |     |     | Thisviewgivesno |     |     |        |       |        |        |          |     |          |       |
| -------------------------------- | --- | --- | --- | --- | --------------- | --- | --- | ------ | ----- | ------ | ------ | -------- | --- | -------- | ----- |
|                                  |     |     |     |     |                 |     |     | On the | basis | of the | Theory | Building |     | View the | decay |
supporttoanexpectationthatprogrammodificationsat
low cost are generally possible. of a program text as a result of modifications made by
|     |     |     |     |     |     |     |     | programmers    |     | without         | a proper | grasp | of          | the underlying |             |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --------------- | -------- | ----- | ----------- | -------------- | ----------- |
|     |     |     |     |     |     |     |     | theory becomes |     | understandable. |          |       | As a matter |                | of fact, if |
Afurthercloselyrelatedissueisthatofprogramflex-
|     |     |     |     |     |     |     |     | viewed merely |     | as a change |     | of the | program | text | and of |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | --- | ------ | ------- | ---- | ------ |
ibility. Inincludingflexibilityinaprogramwebuildinto
|     |     |     |     |     |     |     |     | the external | behaviour |     | of the | execution, |     | a given | desired |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | ------ | ---------- | --- | ------- | ------- |
theprogramcertainoperationalfacilitiesthatarenotim-
mediately demanded, but which are likely to turn out to modification may usually be realized in many different
|            |      |            |         |     |         |        |      | ways, all     | correct. | At     | the same | time, | if viewed | in  | relation  |
| ---------- | ---- | ---------- | ------- | --- | ------- | ------ | ---- | ------------- | -------- | ------ | -------- | ----- | --------- | --- | --------- |
| be useful. | Thus | a flexible | program | is  | able to | handle | cer- |               |          |        |          |       |           |     |           |
|            |      |            |         |     |         |        |      | to the theory |          | of the | program  | these | ways      | may | look very |
tainclassesofchangesofexternalcircumstanceswithout
being modified. different, some of them perhaps conforming to that the-
|     |     |     |     |     |     |     |     | ory or extending |     | it in | a natural |     | way, while | others | may |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ----- | --------- | --- | ---------- | ------ | --- |
It is often stated that programs should be designed be wholly inconsistent with that theory, perhaps having
|                              |       |                 |     |                     |            |     |        | the character   |     | of unintegrated |            | patches | on           | the main | part    |
| ---------------------------- | ----- | --------------- | --- | ------------------- | ---------- | --- | ------ | --------------- | --- | --------------- | ---------- | ------- | ------------ | -------- | ------- |
| to include                   | a lot | of flexibility, | so  | as to               | be readily |     | adapt- |                 |     |                 |            |         |              |          |         |
|                              |       |                 |     |                     |            |     |        | of the program. |     | This            | difference |         | of character | of       | various |
| abletochangingcircumstances. |       |                 |     | Suchadvicemayberea- |            |     |        |                 |     |                 |            |         |              |          |         |
sonable as far as flexibility that can be easily achieved changes is one that can only make sense to the program-
|               |     |          |             |     |     |         |      | mer who | possesses | the | theory | of  | the program. |     | At the |
| ------------- | --- | -------- | ----------- | --- | --- | ------- | ---- | ------- | --------- | --- | ------ | --- | ------------ | --- | ------ |
| is concerned. |     | However, | flexibility | can | in  | general | only |         |           |     |        |     |              |     |        |
be achieved at a substantial cost. Each item of it has same time the character of changes made in a program
|                 |         |           |               |               |           |     |        | text is vital | to  | the longer | term | viability |       | of the    | program. |
| --------------- | ------- | --------- | ------------- | ------------- | --------- | --- | ------ | ------------- | --- | ---------- | ---- | --------- | ----- | --------- | -------- |
| to be designed, |         | including | what          | circumstances |           | it  | has to |               |     |            |      |           |       |           |          |
|                 |         |           |               |               |           |     |        | For a program |     | to retain  | its  | quality   | it is | mandatory | that     |
| cover and       | by what | kind      | of parameters |               | it should | be  | con-   |               |     |            |      |           |       |           |          |
trolled. Then it has to be implemented, tested, and de- each modification is firmly grounded in the theory of it.
|     |     |     |     |     |     |     |     | Indeed, | the very | notion | of  | qualities | such | as simplicity |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | -------- | ------ | --- | --------- | ---- | ------------- | --- |
scribed. Thiscostisincurredinachievingaprogramfea-
ture whose usefulness depends entirely on future events. and good structure can only be understood in terms of
Itmustbeobviousthatbuilt–inprogramflexibilityisno the theory of the program, since they characterize the
|           |             |        |     |              |     |          |     | actual program |     | text | in relation | to  | such | program | texts |
| --------- | ----------- | ------ | --- | ------------ | --- | -------- | --- | -------------- | --- | ---- | ----------- | --- | ---- | ------- | ----- |
| answer to | the general | demand |     | for adapting |     | programs | to  |                |     |      |             |     |      |         |       |
the changing circumstances of the world. that might have been written to achieve the same exe-
|                    |         |              |           |                    |      |            |        | cution behaviour, |       | but            | which | exist   | only as | possibilities | in  |
| ------------------ | ------- | ------------ | --------- | ------------------ | ---- | ---------- | ------ | ----------------- | ----- | -------------- | ----- | ------- | ------- | ------------- | --- |
|                    |         |              |           |                    |      |            |        | the programmer’s  |       | understanding. |       |         |         |               |     |
| In a               | program | modification |           | an existing        |      | programmed |        |                   |       |                |       |         |         |               |     |
| solution           | has to  | be changed   | so as     | to cater           | for  | a change   | in     |                   |       |                |       |         |         |               |     |
| the real           | world   | activity     | it has to | match.             | What | is needed  |        |                   |       |                |       |         |         |               |     |
|                    |         |              |           |                    |      |            |        | Program           | Life, | Death,         | and   | Revival |         |               |     |
| in a modification, |         | first        | of all,   | is a confrontation |      |            | of the |                   |       |                |       |         |         |               |     |
existing solution with the demands called for by the de- A main claim of the Theory Building View of program-
sired modification. In this confrontation the degree and ming is that an essential part of any program, the the-
kind of similarity between the capabilities of the exist- ory of it, is something that could not conceivably be ex-
ing solution and the new demands has to be determined. pressed, but is inextricably bound to human beings. It
Thisneedforadeterminationofsimilaritybringsoutthe follows that in describing the state of the program it is
meritoftheTheoryBuildingView. Indeed,preciselyina important to indicate the extent to which programmers
determination of similarity the shortcoming of any view having its theory remain in charge of it. As a way in
of programming that ignores the central requirement for which to emphasize this circumstance one might extend
the direct participation of persons who possess the ap- the notion of program building by notions of program
propriate insight becomes evident. The point is that the life, death, and revival. The building of the program is
kind of similarity that has to be recognized is accessible the same as the building of the theory of it by and in
to the human beings who possess the theory of the pro- the team of programmers. During the program life a
gram, although entirely outside the reach of what can programmerteampossessingitstheoryremainsinactive
be determined by rules, since even the criteria on which control of the program, and in particular retains control
to judge it cannot be formulated. From the insight into over all modifications. The death of a program happens
the similarity between the new requirements and those when the programmer team possessing its theory is dis-
alreadysatisfiedbytheprogram,theprogrammerisable solved. A dead program may continue to be used for
to design the change of the program text needed to im- execution in a computer and to produce useful results.
plement the modification. Theactualstateofdeathbecomesvisiblewhendemands
4

for modifications of the program cannot be intelligently differ from the original theory behind the program text.
| answered. | Revival | of         | a program |       | is the | rebuilding | of its |         |          |              |            |          |             |      |         |
| --------- | ------- | ---------- | --------- | ----- | ------ | ---------- | ------ | ------- | -------- | ------------ | ---------- | -------- | ----------- | ---- | ------- |
|           |         |            |           |       |        |            |        | Similar | problems |              | are likely | to       | arise even  | when | a pro-  |
| theory by | a new   | programmer |           | team. |        |            |        |         |          |              |            |          |             |      |         |
|           |         |            |           |       |        |            |        | gram is | kept     | continuously |            | alive by | an evolving |      | team of |
Theextendedlifeofaprogramaccordingtotheseno- programmers,asaresultofthedifferencesofcompetence
tions depends on the taking over by new generations of and background experience of the individual program-
programmers of the theory of the program. For a new mers, particularly as the team is being kept operational
|                |       |              |             |     |             |         |             | by inevitable |     | replacements |          | of the | individual | members. |     |
| -------------- | ----- | ------------ | ----------- | --- | ----------- | ------- | ----------- | ------------- | --- | ------------ | -------- | ------ | ---------- | -------- | --- |
| programmer     | to    | come         | to possess  |     | an existing |         | theory of a |               |     |              |          |        |            |          |     |
| program        | it is | insufficient | that        | he  | or she      | has the | opportu-    |               |     |              |          |        |            |          |     |
| nity to become |       | familiar     | with        | the | program     | text    | and other   |               |     |              |          |        |            |          |     |
|                |       |              |             |     |             |         |             | Method        | and | Theory       | Building |        |            |          |     |
| documentation. |       | What         | is required |     | is that     | the     | new pro-    |               |     |              |          |        |            |          |     |
grammer has the opportunity to work in close contact Recent years has seen much interest in programming
|          |             |     |     |         |         |     |             | methods. | In  | the present | section | some | comments |     | will be |
| -------- | ----------- | --- | --- | ------- | ------- | --- | ----------- | -------- | --- | ----------- | ------- | ---- | -------- | --- | ------- |
| with the | programmers |     | who | already | possess |     | the theory, |          |     |             |         |      |          |     |         |
so as to be able to become familiar with the place of the made on the relation between the Theory Building View
program in the wider context of the relevant real world and the notions behind programming methods.
| situations | and   | so as to | acquire | the | knowledge |           | of how the |                                       |     |      |             |     |         |     |        |
| ---------- | ----- | -------- | ------- | --- | --------- | --------- | ---------- | ------------------------------------- | --- | ---- | ----------- | --- | ------- | --- | ------ |
|            |       |          |         |     |           |           |            | Tobeginwith,whatisaprogrammingmethod? |     |      |             |     |         |     | This   |
| program    | works | and how  | unusual |     | program   | reactions | and        |                                       |     |      |             |     |         |     |        |
|            |       |          |         |     |           |           |            | is not always                         |     | made | clear, even | by  | authors | who | recom- |
program modifications are handled within the program mendaparticularmethod. Hereaprogrammingmethod
| theory. | This | problem | of education |     | of new | programmers |     |         |       |         |        |      |           |              |     |
| ------- | ---- | ------- | ------------ | --- | ------ | ----------- | --- | ------- | ----- | ------- | ------ | ---- | --------- | ------------ | --- |
|         |      |         |              |     |        |             |     | will be | taken | to be a | set of | work | rules for | programmers, |     |
inanexistingtheoryofaprogramisquitesimilartothat
|                    |     |              |            |          |            |           |           | telling    | what kind | of        | things    | the programmers |           |         | should do, |
| ------------------ | --- | ------------ | ---------- | -------- | ---------- | --------- | --------- | ---------- | --------- | --------- | --------- | --------------- | --------- | ------- | ---------- |
| of the educational |     | problem      |            | of other | activities |           | where the |            |           |           |           |                 |           |         |            |
|                    |     |              |            |          |            |           |           | in what    | order,    | which     | notations | or              | languages | to      | use, and   |
| knowledge          | of  | how to       | do certain |          | things     | dominates | over      |            |           |           |           |                 |           |         |            |
|                    |     |              |            |          |            |           |           | what kinds | of        | documents | to        | produce         | at        | various | stages.    |
| the knowledge      |     | that certain |            | things   | are        | the case, | such as   |            |           |           |           |                 |           |         |            |
writing and playing a music instrument. The most im- In comparing this notion of method with the Theory
portant educational activity is the student’s doing the Building View of programming, the most important is-
relevant things under suitable supervision and guidance. sueisthatofactionsoroperationsandtheirordering. A
In the case of programming the activity should include method implies a claim that program development can
discussions of the relation between the program and the and should proceed as a sequence of actions of certain
relevant aspects and activities of the real world, and of kinds, each action leading to a particular kind of docu-
thelimitssetontherealworldmattersdealtwithbythe mented result. In building the theory there can be no
program. particular sequence of actions, for the reason that a the-
|     |     |     |     |     |     |     |     | ory held | by a | person | has no | inherent | division |     | into parts |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---- | ------ | ------ | -------- | -------- | --- | ---------- |
AveryimportantconsequenceoftheTheoryBuilding and no inherent ordering. Rather, the person possessing
| View is   | that        | program | revival, | that        | is reestablishing  |     | the      |           |      |           |            |             |               |              |          |
| --------- | ----------- | ------- | -------- | ----------- | ------------------ | --- | -------- | --------- | ---- | --------- | ---------- | ----------- | ------------- | ------------ | -------- |
|           |             |         |          |             |                    |     |          | a theory  | will | be able   | to produce |             | presentations |              | of vari- |
| theory of | a program   |         | merely   | from        | the documentation, |     | is       |           |      |           |            |             |               |              |          |
|           |             |         |          |             |                    |     |          | ous sorts | on   | the basis | of it,     | in response |               | to questions | or       |
| strictly  | impossible. | Lest    | this     | consequence |                    | may | seem un- |           |      |           |            |             |               |              |          |
demands.
reasonableitmaybenotedthattheneedforrevivalofan
entirely dead program probably will rarely arise, since it As to the use of particular kinds of notation or for-
is hardly conceivable that the revival would be assigned malization,againthiscanonlybeasecondaryissuesince
to new programmers without at least some knowledge of the primary item, the theory, is not, and cannot be, ex-
|                                                   |     |           |          |                |     |            |          | pressed,   | and so | no question |            | of the | form     | of its | expression |
| ------------------------------------------------- | --- | --------- | -------- | -------------- | --- | ---------- | -------- | ---------- | ------ | ----------- | ---------- | ------ | -------- | ------ | ---------- |
| the theory                                        | had | by the    | original | team.          |     | Even so    | the The- |            |        |             |            |        |          |        |            |
| oryBuildingViewsuggestsstronglythatprogramrevival |     |           |          |                |     |            |          | arises.    |        |             |            |        |          |        |            |
| should only                                       | be  | attempted |          | in exceptional |     | situations | and      |            |        |             |            |        |          |        |            |
|                                                   |     |           |          |                |     |            |          | It follows |        | that on     | the Theory |        | Building | View,  | for the    |
withfullawarenessthatitisatbestcostly,andmaylead
|              |        |     |              |     |          |     |            | primary | activity | of  | the programming |     | there |     | can be no |
| ------------ | ------ | --- | ------------ | --- | -------- | --- | ---------- | ------- | -------- | --- | --------------- | --- | ----- | --- | --------- |
| to a revived | theory |     | that differs |     | from the | one | originally |         |          |     |                 |     |       |     |           |
right method.
hadbytheprogramauthorsandsomaycontaindiscrep-
ancies with the program text. Thisconclusionmayseemtoconflictwithestablished
|     |     |     |     |     |     |     |     | opinion, | in several | ways, | and | might | thus | be taken | to be |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | ----- | --- | ----- | ---- | -------- | ----- |
Inpreferencetoprogramrevival,theTheoryBuilding
|                |     |              |     |         |      |        |         | an argument   |     | against        | the Theory |       | Building | View. | Two       |
| -------------- | --- | ------------ | --- | ------- | ---- | ------ | ------- | ------------- | --- | -------------- | ---------- | ----- | -------- | ----- | --------- |
| View suggests, |     | the existing |     | program | text | should | be dis- |               |     |                |            |       |          |       |           |
|                |     |              |     |         |      |        |         | such apparent |     | contradictions |            | shall | be taken | up    | here, the |
cardedandthenew–formedprogrammerteamshouldbe
|           |             |          |          |     |               |         |             | first relating | to   | the importance |            | of           | method      | in the | pursuit |
| --------- | ----------- | -------- | -------- | --- | ------------- | ------- | ----------- | -------------- | ---- | -------------- | ---------- | ------------ | ----------- | ------ | ------- |
| given the | opportunity |          | to solve | the | given         | problem | afresh.     |                |      |                |            |              |             |        |         |
|           |             |          |          |     |               |         |             | of science,    | the  | second         | concerning |              | the success | of     | methods |
| Such a    | procedure   | is more  | likely   | to  | produce       | a       | viable pro- |                |      |                |            |              |             |        |         |
|           |             |          |          |     |               |         |             | as actually    | used | in software    |            | development. |             |        |         |
| gram than | program     | revival, |          | and | at no higher, |         | and possi-  |                |      |                |            |              |             |        |         |
bly lower, cost. The point is that building a theory to fit The first argument is that software development
and support an existing program text is a difficult, frus- shouldbebasedonscientificmanners,andsoshouldem-
trating, andtimeconsumingactivity. Thenewprogram- ploy procedures similar to scientific methods. The flaw
mer is likely to feel torn between loyalty to the existing of this argument is the assumption that there is such a
program text, with whatever obscurities and weaknesses thing as scientific method and that it is helpful to scien-
it may contain, and the new theory that he or she has to tists. This question has been the subject of much debate
build up, and which, for better or worse, most likely will in recent years, and the conclusion of such authors as
5

Feyerabend [2], taking his illustrations from the history The contrast between the Theory Building View and
of physics, and Medawar [5], arguing as a biologist, is the more prevalent view of the programmers’ personal
that the notion of scientific method as a set of guidelines contribution is apparent in much of the common discus-
for the practising scientist is mistaken. sion of programming. As just one example, consider the
|                   |                |                                     |                  |                |         |              |          | study of        | modifiability |                 | of large | software            |             | systems     | by Os-     |
| ----------------- | -------------- | ----------------------------------- | ---------------- | -------------- | ------- | ------------ | -------- | --------------- | ------------- | --------------- | -------- | ------------------- | ----------- | ----------- | ---------- |
| This              | conclusion     | is                                  | not contradicted |                | by      | such         | work as  |                 |               |                 |          |                     |             |             |            |
|                   |                |                                     |                  |                |         |              |          | karsson         | [7]. This     | study           | gives    | extensive           |             | information | on         |
| that of           | Polya [8,      | 9] on                               | problem          | solving.       |         | This work    | takes    |                 |               |                 |          |                     |             |             |            |
|                   |                |                                     |                  |                |         |              |          | a considerable  |               | number          | of       | modifications       |             | in one      | release    |
| its illustrations |                | from the                            | field            | of mathematics |         | and          | leads    |                 |               |                 |          |                     |             |             |            |
|                   |                |                                     |                  |                |         |              |          | of a large      | commercial    |                 | system.  | The                 | description |             | covers     |
| to insight        | which          | is also                             | highly           | relevant       | to      | programming. |          |                 |               |                 |          |                     |             |             |            |
|                   |                |                                     |                  |                |         |              |          | the background, |               | substance,      |          | and implementation, |             |             | of each    |
| However,          | it cannot      | be                                  | claimed          | to             | present | a method     | on       |                 |               |                 |          |                     |             |             |            |
|                   |                |                                     |                  |                |         |              |          | modification,   |               | with particular |          | attention           |             | to the      | manner     |
| whichtoproceed.   |                | Rather,itisacollectionofsuggestions |                  |                |         |              |          |                 |               |                 |          |                     |             |             |            |
|                   |                |                                     |                  |                |         |              |          | in which        | the program   |                 | changes  | are                 | confined    | to          | particu-   |
| aiming            | at stimulating |                                     | the mental       | activity       |         | of the       | problem  |                 |               |                 |          |                     |             |             |            |
|                   |                |                                     |                  |                |         |              |          | lar program     | modules.      |                 | However, |                     | there       | is no       | suggestion |
| solver,           | by pointing    | out                                 | different        | modes          | of      | work         | that may |                 |               |                 |          |                     |             |             |            |
whatsoeverthattheimplementationofthemodifications
| be applied | in any | sequence. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
mightdependonthebackgroundofthe500programmers
The second argument that may seem to contradict employed on the project, such as the length of time they
the dismissal of method of the Theory Building View is have been working on it, and there is no indication of
that the use of particular methods has been successful, the manner in which the design decisions are distributed
|           |              |     |          |     |               |     |        | among | the 500 | programmers. |     | Even | so  | the significance |     |
| --------- | ------------ | --- | -------- | --- | ------------- | --- | ------ | ----- | ------- | ------------ | --- | ---- | --- | ---------------- | --- |
| according | to published |     | reports. | To  | this argument |     | it may |       |         |              |     |      |     |                  |     |
be answered that a methodically satisfactory study of of an underlying theory is admitted indirectly in state-
the efficacy of programming methods so far never seems ments such as that ‘decisions were implemented in the
to have been made. Such a study would have to em- wrongblock’andinareferenceto‘aphilosophyofAXE’.
ploy the well established technique of controlled exper- However,bythemannerinwhichthestudyisconducted
|            |              |         |              |             |                |                |        | these admissions |            | can  | only remain |     | isolated   | indications. |          |
| ---------- | ------------ | ------- | ------------ | ----------- | -------------- | -------------- | ------ | ---------------- | ---------- | ---- | ----------- | --- | ---------- | ------------ | -------- |
| iments     | (cf. Brooks, | 1980    | [1]          | or Moher    |                | and Schneider, |        |                  |            |      |             |     |            |              |          |
| 1982 [6]). | The          | lack of | such studies |             | is explainable |                | partly |                  |            |      |             |     |            |              |          |
|            |              |         |              |             |                |                |        | More             | generally, | much | current     |     | discussion | of           | program- |
| by the     | high cost    | that    | would        | undoubtedly |                | be incurred    | in     |                  |            |      |             |     |            |              |          |
mingseemstoassumethatprogrammingissimilartoin-
| such investigations |     | if  | the results | were | to  | be significant, |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | ----------- | ---- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
dustrialproduction,theprogrammerbeingregardedasa
| partly by    | the problems |            | of establishing |          | in   | an operational |         |               |                                     |                  |              |             |     |       |            |
| ------------ | ------------ | ---------- | --------------- | -------- | ---- | -------------- | ------- | ------------- | ----------------------------------- | ---------------- | ------------ | ----------- | --- | ----- | ---------- |
|              |              |            |                 |          |      |                |         | component     | of                                  | that production, |              | a component |     | that  | has to     |
| fashion      | the concepts | underlying |                 | what     | is   | called         | methods |               |                                     |                  |              |             |     |       |            |
|              |              |            |                 |          |      |                |         | be controlled | by                                  | rules            | of procedure |             | and | which | can be re- |
| in the field | of program   |            | development.    |          | Most | published      | re-     |               |                                     |                  |              |             |     |       |            |
|              |              |            |                 |          |      |                |         | placedeasily. | Anotherrelatedviewisthathumanbeings |                  |              |             |     |       |            |
| ports on     | such         | methods    | merely          | describe |      | and recommend  |         |               |                                     |                  |              |             |     |       |            |
performbestiftheyactlikemachines,byfollowingrules,
| certain          | techniques | and         | procedures, |     | without    | establishing |         |        |            |        |     |        |       |                |     |
| ---------------- | ---------- | ----------- | ----------- | --- | ---------- | ------------ | ------- | ------ | ---------- | ------ | --- | ------ | ----- | -------------- | --- |
|                  |            |             |             |     |            |              |         | with a | consequent | stress | on  | formal | modes | of expression, |     |
| their usefulness |            | or efficacy | in          | any | systematic |              | way. An |        |            |        |     |        |       |                |     |
whichmakeitpossibletoformulatecertainargumentsin
| elaborate   | study      | of five | different     | methods |       | by        | C. Floyd  |           |             |           |               |        |      |       |         |
| ----------- | ---------- | ------- | ------------- | ------- | ----- | --------- | --------- | --------- | ----------- | --------- | ------------- | ------ | ---- | ----- | ------- |
|             |            |         |               |         |       |           |           | terms of  | rules       | of formal | manipulation. |        | Such | views | agree   |
| and several | co–workers |         | [3] concludes |         | that  | the       | notion of |           |             |           |               |        |      |       |         |
|             |            |         |               |         |       |           |           | well with | the notion, |           | seemingly     | common |      | among | persons |
| methods     | as systems | of      | rules         | that    | in an | arbitrary | con-      |           |             |           |               |        |      |       |         |
workingwithcomputers,thatthehumanmindworkslike
| text and   | mechanically    |            | will lead | to       | good       | solutions | is an    |                     |                                       |          |             |                  |     |         |           |
| ---------- | --------------- | ---------- | --------- | -------- | ---------- | --------- | -------- | ------------------- | ------------------------------------- | -------- | ----------- | ---------------- | --- | ------- | --------- |
|            |                 |            |           |          |            |           |          | acomputer.          | Atthelevelofindustrialmanagementthese |          |             |                  |     |         |           |
| illusion.  | What            | remains    | is the    | effect   | of         | methods   | in the   |                     |                                       |          |             |                  |     |         |           |
|            |                 |            |           |          |            |           |          | views support       |                                       | treating | programmers |                  | as  | workers | of fairly |
| education  | of programmers. |            |           | This     | conclusion | is        | entirely |                     |                                       |          |             |                  |     |         |           |
|            |                 |            |           |          |            |           |          | low responsibility, |                                       | and      | only        | brief education. |     |         |           |
| compatible | with            | the Theory |           | Building | View       | of        | program- |                     |                                       |          |             |                  |     |         |           |
ming. Indeed,onthisviewthequalityofthetheorybuilt
|     |     |     |     |     |     |     |     | On  | the Theory | Building |     | View | the primary |     | result of |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | ---- | ----------- | --- | --------- |
by the programmer will depend to a large extent on the the programming activity is the theory held by the pro-
programmer’s familiarity with model solutions of typical grammers. Since this theory by its very nature is part of
problems,withtechniquesofdescriptionandverification,
thementalpossessionofeachprogrammer,itfollowsthat
and with principles of structuring systems consisting of the notion of the programmer as an easily replaceable
| many parts | in  | complicated | interactions. |     |     | Thus | many of |           |     |             |     |            |          |     |           |
| ---------- | --- | ----------- | ------------- | --- | --- | ---- | ------- | --------- | --- | ----------- | --- | ---------- | -------- | --- | --------- |
|            |     |             |               |     |     |      |         | component | in  | the program |     | production | activity |     | has to be |
the items of concern of methods are relevant to theory abandoned. Instead the programmer must be regarded
building. WheretheTheoryBuildingViewdepartsfrom asaresponsibledeveloperandmanageroftheactivityin
| that of | the methodologists |     | is  | on the | question |     | of which |                          |     |     |     |                           |     |     |     |
| ------- | ------------------ | --- | --- | ------ | -------- | --- | -------- | ------------------------ | --- | --- | --- | ------------------------- | --- | --- | --- |
|         |                    |     |     |        |          |     |          | whichthecomputerisapart. |     |     |     | Inordertofillthisposition |     |     |     |
techniques to use and in what order. On the Theory heorshemustbegivenapermanentposition,ofastatus
BuildingViewthismustremainentirelyamatterforthe
|            |     |         |        |      |         |     |        | similar      | to that | of other | professionals, |     | such | as           | engineers |
| ---------- | --- | ------- | ------ | ---- | ------- | --- | ------ | ------------ | ------- | -------- | -------------- | --- | ---- | ------------ | --------- |
| programmer | to  | decide, | taking | into | account | the | actual |              |         |          |                |     |      |              |           |
|            |     |         |        |      |         |     |        | and lawyers, | whose   | active   | contributions  |     |      | as employers | of        |
problem to be solved. enterprises rest on their intellectual proficiency.
|              |     |        |         |        |          |     |      | The    | raising | of the   | status | of programmers |      |       | suggested |
| ------------ | --- | ------ | ------- | ------ | -------- | --- | ---- | ------ | ------- | -------- | ------ | -------------- | ---- | ----- | --------- |
| Programmers’ |     | Status | and the | Theory | Building |     | View |        |         |          |        |                |      |       |           |
|              |     |        |         |        |          |     |      | by the | Theory  | Building | View   | will           | have | to be | supported |
The areas where the consequences of the Theory Build- by a corresponding reorientation of the programmer ed-
ing View contrast most strikingly with those of the more ucation. While skills such as the mastery of notations,
prevalent current views are those of the programmers’ data representations, and data processes, remain impor-
personalcontributiontotheactivityandoftheprogram- tant, the primary emphasis would have to turn in the
mers’ proper status. direction of furthering the understanding and talent for
6

theory formation. To what extent this can be taught at ecution of a program. Such a view leads to a notion of
all must remain an open question. The most hopeful ap- program life that depends on the continued support of
proach would be to have the student work on concrete theprogrambyprogrammershavingitstheory. Further,
problems under guidance, in an active and constructive on this view the notion of a programming method, un-
environment. derstood as a set of rules of procedure to be followed by
|     |     |     |     |     |     |     |     | the programmer, |           | is  | based      | on invalid   | assumptions | and so       |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------- | --------- | --- | ---------- | ------------ | ----------- | ------------ |
|     |     |     |     |     |     |     |     | has to be       | rejected. |     | As further | consequences |             | of the view, |
Conclusions
|     |     |     |     |     |     |     |     | programmers |     | have to | be accorded | the | status | of responsi- |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ----------- | --- | ------ | ------------ |
Acceptingprogrammodificationsdemandedbychanging ble, permanent developers and managers of the activity
external circumstances to be an essential part of pro- of which the computer is a part, and their education has
gramming,itisarguedthattheprimaryaimofprogram- toemphasizetheexerciseoftheorybuilding, sidebyside
ming is to have the programmers build a theory of the with the acquisition of knowledge of data processing and
notations.
| way the | matters | at  | hand | may be | supported | by  | the ex- |     |     |     |     |     |     |     |
| ------- | ------- | --- | ---- | ------ | --------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
References
1. Brooks, R. E. Studying programmer behaviour experimentally. Comm. ACM 23(4): 207–213, 1980.
2. Feyerabend, P. Against Method. London, Verso Editions, 1978; ISBN: 86091–700–2.
3. Floyd, C. Eine Untersuchung von Software–Entwicklungs–Methoden. Pp. 248–274 in Programmierumgebungen
und Compiler, ed H. Morgenbrod and W. Sammer, Tagung I/1984 des German Chapter of the ACM, Stuttgart,
| Teubner |     | Verlag, | 1984; | ISBN: | 3–519–02437–3. |     |     |     |     |     |     |     |     |     |
| ------- | --- | ------- | ----- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
4. Kuhn,T.S.TheStructureofScientificRevolutions,SecondEdition. Chicago,UniversityofChicagoPress,1970;
| ISBN: | 0–226–45803–2. |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5. Medawar, P. Pluto’s Republic. Oxford, University Press, 1982: ISBN: 0–19–217726–5.
6. Moher, T., and Schneider, G. M. Methodology and experimental research in software engineering, Int. J.
| Man–Mach. |     | Stud. | 16: | 65–87, | 1. Jan. | 1982. |     |     |     |     |     |     |     |     |
| --------- | --- | ----- | --- | ------ | ------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
7. Oskarsson,O¨ MechanismsofmodifiabilityinlargesoftwaresystemsLink¨opingStudiesinScienceandTechnology,
| Dissertations, |     |     | no. 77,  | Link¨oping, |       | 1982; ISBN:     | 91–7372–527–7. |              |       |     |     |     |     |     |
| -------------- | --- | --- | -------- | ----------- | ----- | --------------- | -------------- | ------------ | ----- | --- | --- | --- | --- | --- |
| 8. Polya,      | G.  | How | To Solve | It          | . New | York, Doubleday |                | Anchor Book, | 1957. |     |     |     |     |     |
9. Polya, G. Mathematics and Plausible Reasoning. New Jersey, Princeton University Press, 1954.
10. Popper, K. R., and Eccles, J. C. The Self and Its Brain. London, Routledge and Kegan Paul, 1977.
11. Ryle, G. The Concept of Mind. Harmondsworth, England, Penguin, 1963, first published 1949. Applying
| “Theory |     | Building” |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Applying “Theory Building” If “assembly line” is an appropriate metaphor, then
laterprogrammers,consideringwhattheyknowaboutas-
Viewingprogrammingastheorybuildinghelpsusunder-
semblylines,willmakeguessesaboutthestructureofthe
stand“metaphorbuilding”activityinExtremeProgram-
|                   |     |     |            |       |        |                 |     | software  | at hand          | and | find | that their     | guesses | are “close.” |
| ----------------- | --- | --- | ---------- | ----- | ------ | --------------- | --- | --------- | ---------------- | --- | ---- | -------------- | ------- | ------------ |
| ming (XP),        | and | the | respective | roles | of     | tacit knowledge |     |           |                  |     |      |                |         |              |
|                   |     |     |            |       |        |                 |     | That is   | an extraordinary |     |      | power for just | the     | two words,   |
| and documentation |     |     | in passing | along | design | knowledge.      |     |           |                  |     |      |                |         |              |
|                   |     |     |            |       |        |                 |     | “assembly | line.”           |     |      |                |         |              |
Thevalueofagoodmetaphorincreaseswiththenum-
| The Metaphor                          |        | as a     | Theory. | Kent   | Beck     | suggested        | that |                 |       |                                     |          |             |     |               |
| ------------------------------------- | ------ | -------- | ------- | ------ | -------- | ---------------- | ---- | --------------- | ----- | ----------------------------------- | -------- | ----------- | --- | ------------- |
|                                       |        |          |         |        |          |                  |      | berofdesigners. |       | Theclosereachperson’sguessis“close” |          |             |     |               |
| it is useful                          | to     | a design | team    | to     | simplify | the general      | de-  |                 |       |                                     |          |             |     |               |
|                                       |        |          |         |        |          |                  |      | to the          | other | people’s                            | guesses, | the greater |     | the resulting |
| signofaprogramtomatchasinglemetaphor. |        |          |         |        |          | Examples         |      |                 |       |                                     |          |             |     |               |
|                                       |        |          |         |        |          |                  |      | consistency     | in    | the final                           | system   | design.     |     |               |
| might be,                             | “This  | program  |         | really | looks    | like an assembly |      |                 |       |                                     |          |             |     |               |
| line, with                            | things | getting  |         | added  | to a     | chassis along    | the  |                 |       |                                     |          |             |     |               |
Imagine10programmersworkingasfastastheycan,
| line,” or    | “This | program    | really |     | looks like | a restaurant, |     |              |        |        |      |                  |     |             |
| ------------ | ----- | ---------- | ------ | --- | ---------- | ------------- | --- | ------------ | ------ | ------ | ---- | ---------------- | --- | ----------- |
|              |       |            |        |     |            |               |     | in parallel, | each   | making |      | design decisions |     | and adding  |
| with waiters |       | and menus, | cooks  | and | cashiers.” |               |     |              |        |        |      |                  |     |             |
|              |       |            |        |     |            |               |     | classes      | as she | goes.  | Each | will necessarily |     | develop her |
If the metaphor is good, the many associations the own theory as she goes. As each adds code, the the-
orythatbindstheirworkbecomeslessandlesscoherent,
| designers | create   | around      | the | metaphor | turn       | out to | be ap- |                                   |      |              |     |          |                 |      |
| --------- | -------- | ----------- | --- | -------- | ---------- | ------ | ------ | --------------------------------- | ---- | ------------ | --- | -------- | --------------- | ---- |
|           |          |             |     |          |            |        |        | more and                          | more | complicated. |     | Not only | maintenance     | gets |
| propriate | to their | programming |     |          | situation. |        |        |                                   |      |              |     |          |                 |      |
|           |          |             |     |          |            |        |        | harder,buttheirownworkgetsharder. |      |              |     |          | Thedesigneasily |      |
That is exactly Naur’s idea of passing along a theory becomes a “kludge.” If they have a common theory, on
of the design. the other hand, they add code in ways that fit together.
7

An appropriate, shared metaphor lets a person guess gorithm, a second is like an accounting ledger, the user
accurately where someone else on the team just added interface follows the model-observer design pattern, and
| code, and       | how    | to fit    | her new        | piece in | with it.      |          | so on.      |      |           |       |       |       |            |
| --------------- | ------ | --------- | -------------- | -------- | ------------- | -------- | ----------- | ---- | --------- | ----- | ----- | ----- | ---------- |
|                 |        |           |                |          |               |          | Experienced |      | designers | often | start | their | documenta- |
| Tacit Knowledge |        | and       | Documentation. |          | The           | documen- |             |      |           |       |       |       |            |
|                 |        |           |                |          |               |          | tion with   | just |           |       |       |       |            |
| tation is       | almost | certainly | behind         | the      | current state | of the   |             |      |           |       |       |       |            |
program, but people are good at looking around. What • The metaphors
should you put into the documentation? • Text describing the purpose of each major compo-
nent
| That | which | helps | the next | programmer | build | an ad- |     |     |     |     |     |     |     |
| ---- | ----- | ----- | -------- | ---------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
• Drawingsofthemajorinteractionsbetweenthema-
| equate theory |               | of the | program.   |     |             |        |     |            |     |     |     |     |     |
| ------------- | ------------- | ------ | ---------- | --- | ----------- | ------ | --- | ---------- | --- | --- | --- | --- | --- |
|               |               |        |            |     |             |        | jor | components |     |     |     |     |     |
| This          | is enormously |        | important. |     | The purpose | of the |     |            |     |     |     |     |     |
documentation is to jog memories in the reader, set These three items alone take the next team a long
|             |          |     |            |       |             |     | way to constructing |     | a useful | theory | of  | the design. |     |
| ----------- | -------- | --- | ---------- | ----- | ----------- | --- | ------------------- | --- | -------- | ------ | --- | ----------- | --- |
| up relevant | pathways |     | of thought | about | experiences | and |                     |     |          |        |     |             |     |
metaphors.
|     |     |     |     |     |     |     | The source | code | itself      | serves  | to communicate |            | a the- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | ----------- | ------- | -------------- | ---------- | ------ |
|     |     |     |     |     |     |     | ory to the | next | programmer. | Simple, |                | consistent | naming |
Thissortofdocumentationismorestableoverthelife
oftheprogramthanjustnamingthepiecesofthesystem conventions help the next person build a coherent the-
currently in place. ory. When people talk about “clean code,” a large part
|     |     |     |     |     |     |     | of what they | are | referring | to is how | easily | the | reader can |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | --------- | ------ | --- | ---------- |
Thedesignersareallowedtousewhateverformsofex-
|     |     |     |     |     |     |     | build a coherent |     | theory of | the system. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --------- | ----------- | --- | --- | --- |
pressionarenecessarytosetupthoserelevantpathways.
Theycanevenusemultiplemetaphors, iftheydon’tfind Documentationcannot—andsoneednot—sayevery-
one that is adequate for the entire program. They might thing. Its purpose is to help the next programmer build
saythatonesectionimplementsafractalcompressional- an accurate theory about the system.
8
