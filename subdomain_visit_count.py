class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """

        '''
        Time complexity: O(n^2)
        Space Complexit: O(n)
        '''
        d = {}

        for cpdomain in cpdomains:
            count, link = cpdomain.split(' ')
            domain_list = link.split('.')
            n = len(domain_list)
            for i in range(0,n):
                domain = '.'.join(domain_list[i:])
                d[domain] = d.get(domain,0) + int(count)

        return ['{} {}'.format(value,key) for key,value in d.items()]
