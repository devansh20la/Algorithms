class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []
        for email in emails:
            local_name, domain_name = email.split("@")
            
            local_name = local_name.replace(".","")
            new_local_name = ""
            for i in local_name:
                if i == '+':
                    break
                else:
                    new_local_name = new_local_name + i
            email = new_local_name + "@" + domain_name
            if email not in res:
                res.append(email)
        
        return len(res)
                
        