import unittest



def evaluate(age, income, credit_score, emp):

    # BẮT NGOẠI LỆ

    if age < 18 or age > 65:
        return "Invalid Input"
    if income < 5.0 or income > 500.0:
        return "Invalid Input"
    if credit_score < 300 or credit_score > 850:
        return "Invalid Input"
    if emp not in ["C", "F"]:
        return "Invalid Input"

    # XÁC ĐỊNH MỨC ĐỘ RỦI RO

    risk = ""
    if 300 <= credit_score <= 500:
        risk = "High"
    elif 501 <= credit_score <= 700:
        risk = "Medium"
    elif 701 <= credit_score <= 850:
        risk = "Low"

    # XỬ LÝ LOGIC NGHIỆP VỤ

    if risk == "High":
        return "REJECT"

    if risk == "Medium" and income < 15.0:
        return "REJECT"

    if risk == "Low" and income < 15.0 and emp == "F":
        return "REJECT"

    if risk == "Low" and income < 15.0 and emp == "C":
        return "MANUAL REVIEW"

    if risk in ["Medium", "Low"] and income >= 15.0 and emp == "C":
        return "APPROVE"

    if risk in ["Medium", "Low"] and income >= 15.0 and emp == "F":
        return "MANUAL REVIEW"

    return "UNKNOWN ERROR"

class TestLoanApprovalSystem(unittest.TestCase):

    # NHÓM 1: KIỂM TRA NGOẠI LỆ (INVALID INPUTS)

    def test_invalid_inputs_age(self):
        self.assertEqual("Invalid Input", evaluate(17, 20.0, 600, "C"))
        self.assertEqual("Invalid Input", evaluate(66, 20.0, 600, "C"))

    def test_invalid_inputs_income(self):
        self.assertEqual("Invalid Input", evaluate(30, 4.9, 600, "C"))
        self.assertEqual("Invalid Input", evaluate(30, 500.1, 600, "C"))

    def test_invalid_inputs_credit_score(self):
        self.assertEqual("Invalid Input", evaluate(30, 20.0, 299, "C"))
        self.assertEqual("Invalid Input", evaluate(30, 20.0, 851, "C"))

    def test_invalid_inputs_employment(self):
        self.assertEqual("Invalid Input", evaluate(30, 20.0, 600, "X"))

    # NHÓM 2: KIỂM TRA LOGIC NGHIỆP VỤ

    def test_business_logic_rule1_high_risk(self):
        self.assertEqual("REJECT", evaluate(18, 5.0, 300, "C"))
        self.assertEqual("REJECT", evaluate(65, 500.0, 500, "F"))

    def test_business_logic_rule2_medium_risk_low_income(self):
        self.assertEqual("REJECT", evaluate(30, 5.0, 501, "C"))
        self.assertEqual("REJECT", evaluate(30, 14.9, 700, "F"))

    def test_business_logic_rule3_low_risk_low_income_freelance(self):
        self.assertEqual("REJECT", evaluate(30, 10.0, 701, "F"))

    def test_business_logic_rule4_low_risk_low_income_contract(self):
        self.assertEqual("MANUAL REVIEW", evaluate(30, 14.9, 850, "C"))

    def test_business_logic_rule5_medlow_risk_high_income_contract(self):
        self.assertEqual("APPROVE", evaluate(30, 15.0, 700, "C"))
        self.assertEqual("APPROVE", evaluate(30, 500.0, 850, "C"))

    def test_business_logic_rule6_medlow_risk_high_income_freelance(self):
        self.assertEqual("MANUAL REVIEW", evaluate(30, 15.0, 501, "F"))
        self.assertEqual("MANUAL REVIEW", evaluate(30, 50.0, 701, "F"))

if __name__ == '__main__':
    unittest.main()