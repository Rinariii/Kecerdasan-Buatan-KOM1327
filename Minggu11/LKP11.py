from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([('Exercise','HeartDisease'),
                         ('Diet','HeartDisease'),
                         ('Diet','HeartBurn'),
                         ('HeartDisease','BloodPressure'),
                         ('HeartDisease','ChestPain'),
                         ('HeartBurn','ChestPain')])

# P(Exercise)
cpd_exercise = TabularCPD(variable='Exercise',variable_card=2,
                          values=[[0.3],[0.7]]) # P(~Exercise) , P(Exrercise)

# P(Diet=Healthy)
cpd_diet = TabularCPD(variable='Diet',variable_card=2,
                      values=[[0.75],[0.25]]) #P(~Diet), P(Diet)

# P(HeartDisease | Exercise, Diet)
cpd_heart_disease = TabularCPD(
    variable='HeartDisease',
    variable_card=2,
    values=[[0.25, 0.45, 0.55, 0.75],[0.75, 0.55, 0.45, 0.25]],
    evidence=['Exercise', 'Diet'],
    evidence_card=[2, 2]
)

# P(HeartBurn | Diet)
cpd_heartburn = TabularCPD(variable='HeartBurn',variable_card=2,
                           values=[[0.15,0.8],[0.85,0.2]],
                           evidence =['Diet'],
                           evidence_card=[2])

# P(BloodPressure | HeartDisease)
cpd_blood_pressure = TabularCPD(variable='BloodPressure',variable_card=2,
                                values=[[0.8,0.15],
                                        [0.2,0.85]],
                                evidence=['HeartDisease'],
                                evidence_card=[2])


# P(ChestPain | HeartDisease , HeartBurn)
cpd_chest_pain = TabularCPD(variable='ChestPain', variable_card=2,
                            values=[[0.9,0.6,0.4,0.2],[0.1,0.4,0.6,0.8]],
                            evidence=['HeartDisease','HeartBurn'],
                            evidence_card=[2,2])

# Masukan cpd ke model
model.add_cpds(cpd_exercise,cpd_diet,cpd_heart_disease,cpd_blood_pressure,cpd_chest_pain,cpd_heartburn)

# Verif model
assert model.check_model()

# Inference
inference = VariableElimination(model)

#Query : Jika diketahui bahwa pasien memiliki High BloodPressure. Berapa peluang pasien itu menderita HeartDisease?
result = inference.query(variables=['HeartDisease'],evidence={'BloodPressure' : 1})
print(result)

#Query :  Jika diketahui bahwa pasien mengalami Chest Pain, berapa peluang pasien melakukan Exercise?
result2 = inference.query(variables=['Exercise'],evidence={'ChestPain' : 1})
print(result2)
