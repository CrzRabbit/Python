'''
给你一个二维数组 tasks ，用于表示 n​​​​​​ 项从 0 到 n - 1 编号的任务。其中 tasks[i] = [enqueueTimei, processingTimei] 意味着第 i​​​​​​​​​​
项任务将会于 enqueueTimei 时进入任务队列，需要 processingTimei 的时长完成执行。

现有一个单线程 CPU ，同一时间只能执行 最多一项 任务，该 CPU 将会按照下述方式运行：

如果 CPU 空闲，且任务队列中没有需要执行的任务，则 CPU 保持空闲状态。
如果 CPU 空闲，但任务队列中有需要执行的任务，则 CPU 将会选择 执行时间最短 的任务开始执行。如果多个任务具有同样的最短执行时间，则选择下标最小的任务开始执行。
一旦某项任务开始执行，CPU 在 执行完整个任务 前都不会停止。
CPU 可以在完成一项任务后，立即开始执行一项新任务。
返回 CPU 处理任务的顺序。

示例 1：
输入：tasks = [[1,2],[2,4],[3,2],[4,1]]
输出：[0,2,3,1]
解释：事件按下述流程运行：
- time = 1 ，任务 0 进入任务队列，可执行任务项 = {0}
- 同样在 time = 1 ，空闲状态的 CPU 开始执行任务 0 ，可执行任务项 = {}
- time = 2 ，任务 1 进入任务队列，可执行任务项 = {1}
- time = 3 ，任务 2 进入任务队列，可执行任务项 = {1, 2}
- 同样在 time = 3 ，CPU 完成任务 0 并开始执行队列中用时最短的任务 2 ，可执行任务项 = {1}
- time = 4 ，任务 3 进入任务队列，可执行任务项 = {1, 3}
- time = 5 ，CPU 完成任务 2 并开始执行队列中用时最短的任务 3 ，可执行任务项 = {1}
- time = 6 ，CPU 完成任务 3 并开始执行任务 1 ，可执行任务项 = {}
- time = 10 ，CPU 完成任务 1 并进入空闲状态

示例 2：
输入：tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
输出：[4,3,2,0,1]
解释：事件按下述流程运行：
- time = 7 ，所有任务同时进入任务队列，可执行任务项  = {0,1,2,3,4}
- 同样在 time = 7 ，空闲状态的 CPU 开始执行任务 4 ，可执行任务项 = {0,1,2,3}
- time = 9 ，CPU 完成任务 4 并开始执行任务 3 ，可执行任务项 = {0,1,2}
- time = 13 ，CPU 完成任务 3 并开始执行任务 2 ，可执行任务项 = {0,1}
- time = 18 ，CPU 完成任务 2 并开始执行任务 0 ，可执行任务项 = {1}
- time = 28 ，CPU 完成任务 0 并开始执行任务 1 ，可执行任务项 = {}
- time = 40 ，CPU 完成任务 1 并进入空闲状态

提示：
tasks.length == n
1 <= n <= 105
1 <= enqueueTimei, processingTimei <= 109
'''
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ret = []
        temp = []
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks = sorted(tasks, key=lambda x: x[0])
        i = 1
        j = 1
        while len(temp) or len(tasks):
            while len(tasks) and i >= tasks[0][0]:
                temp.append(tasks[0][1:])
                tasks = tasks[1:]
            if i == j:
                if len(temp):
                    temp = sorted(temp, key=lambda x: x[0])
                    time = temp[0][0]
                    for a in range(len(temp)):
                        if temp[a][0] > time:
                            for b in range(a - 1, 0, -1):
                                if temp[b][1] < temp[b - 1][1]:
                                    temp[b][1], temp[b - 1][1] = temp[b - 1][1], temp[b][1]
                            break
                    j += temp[0][0]
                    ret.append(temp[0][1])
                    temp = temp[1:]
                else:
                    j += 1
            i += 1
        return ret

tasks = [[492,959],[492,9],[492,609],[492,333],[492,97],[492,424],[492,774],[492,777],[492,811],[492,827],[759,647],[759,159],[638,291],[638,196],[638,826],[822,772],[822,793],[240,100],[240,687],[240,368],[766,171],[766,242],[766,465],[766,382],[766,696],[766,713],[766,746],[766,617],[766,794],[951,220],[716,680],[716,34],[788,215],[788,578],[788,398],[788,769],[788,380],[714,987],[714,994],[714,404],[714,511],[714,411],[714,970],[714,264],[843,297],[843,901],[843,290],[843,201],[843,367],[843,738],[846,346],[67,214],[67,734],[67,379],[67,743],[67,294],[67,824],[67,671],[67,852],[852,122],[852,972],[852,996],[732,120],[732,59],[732,954],[732,745],[732,878],[371,989],[371,121],[920,48],[920,657],[920,794],[920,328],[920,771],[920,64],[920,373],[920,424],[920,34],[628,458],[628,14],[628,892],[628,480],[628,971],[254,981],[254,665],[254,881],[254,679],[254,678],[398,367],[787,72],[654,373],[654,217],[654,638],[164,348],[164,975],[164,176],[67,118],[67,171],[67,12],[67,364],[67,43],[67,820],[67,285],[67,134],[67,538],[282,905],[282,646],[282,52],[282,71],[282,685],[282,953],[282,700],[282,665],[282,694],[970,771],[970,364],[970,97],[794,971],[794,377],[794,253],[794,288],[794,813],[794,56],[794,438],[424,536],[424,589],[424,598],[247,876],[247,220],[573,109],[573,139],[573,424],[573,733],[573,670],[573,55],[573,810],[573,380],[973,870],[462,315],[462,711],[462,278],[462,199],[462,57],[510,444],[962,863],[962,228],[962,812],[962,118],[962,235],[962,703],[962,876],[576,219],[576,342],[576,441],[576,563],[779,865],[779,78],[779,495],[779,168],[779,437],[923,383],[923,934],[923,631],[923,321],[854,150],[854,786],[854,585],[854,593],[81,47],[81,553],[81,118],[81,747],[81,506],[81,871],[81,931],[81,998],[81,41],[364,467],[364,895],[364,530],[364,414],[689,802],[689,971],[689,919],[689,656],[689,166],[411,404],[411,593],[411,937],[411,335],[411,134],[411,117],[411,803],[587,503],[587,759],[587,538],[587,544],[587,438],[587,924],[587,277],[327,731],[615,104],[615,207],[615,313],[615,958],[615,571],[615,143],[615,657],[615,829],[615,984],[615,224],[62,248],[62,567],[62,664],[62,229],[62,649],[62,840],[62,900],[62,174],[62,296],[930,597],[930,682],[930,343],[930,763],[930,728],[930,605],[930,332],[930,447],[930,4],[930,909],[87,697],[87,916],[87,25],[87,94],[87,247],[87,311],[87,494],[587,164],[587,343],[587,713],[587,280],[587,170],[587,994],[587,731],[587,270],[766,450],[766,15],[766,713],[766,470],[766,893],[766,907],[766,745],[766,594],[903,720],[903,797],[903,132],[903,62],[123,150],[64,989],[64,272],[64,692],[72,127],[72,131],[72,251],[72,899],[72,295],[72,220],[72,104],[72,494],[72,597],[72,386],[677,1],[677,580],[677,425],[677,30],[677,237],[677,633],[677,386],[951,166],[951,718],[951,388],[951,782],[951,693],[951,673],[951,869],[951,5],[680,201],[680,841],[680,158],[680,40],[680,708],[680,192],[680,558],[680,268],[356,701],[356,705],[356,388],[356,384],[356,99],[356,772],[356,462],[672,222],[672,200],[672,938],[672,854],[672,339],[321,231],[321,233],[321,958],[766,593],[766,748],[766,293],[766,371],[766,349],[766,997],[766,895],[766,220],[766,615],[766,261],[920,404],[920,688],[920,916],[920,26],[920,691],[920,973],[920,196],[920,687],[920,567],[920,347],[565,695],[565,663],[565,123],[565,6],[565,795],[565,202],[565,460],[565,273],[565,604],[279,975],[279,716],[279,611],[279,216],[279,536],[279,251],[145,856],[502,666],[502,444],[502,18],[502,63],[502,331],[502,829],[237,281],[237,67],[237,405],[237,917],[237,555],[237,828],[237,899],[237,954],[799,214],[799,79],[799,165],[799,208],[799,424],[799,411],[799,325],[865,925],[865,669],[346,684],[346,796],[346,711],[346,885],[346,916],[346,670],[90,866],[90,838],[90,108],[411,550],[411,997],[309,985],[309,849],[309,471],[309,466],[309,31],[309,50],[309,535],[309,907],[229,335],[229,837],[229,372],[229,454],[229,735],[229,736],[229,650],[229,788],[660,835],[919,756],[919,950],[36,530],[36,749],[36,641],[36,819],[36,31],[973,866],[973,720],[973,120],[973,691],[973,945],[973,716],[723,791],[723,514],[723,240],[723,48],[723,251],[723,847],[723,413],[723,925],[528,301],[528,516],[528,611],[528,852],[528,382],[528,643],[528,950],[550,623],[550,325],[550,539],[550,156],[550,448],[550,540],[550,344],[550,900],[550,122],[762,317],[762,320],[762,845],[762,838],[762,713],[762,336],[762,327],[762,954],[145,42],[145,729],[551,779],[551,59],[927,145],[927,729],[927,855],[927,589],[927,112],[927,469],[927,128],[927,212],[161,473],[161,186],[161,215],[161,362],[161,886],[194,846],[194,786],[194,243],[194,886],[194,131],[194,890],[194,554],[194,80],[64,890],[64,861],[64,998],[64,195],[64,63],[64,13],[64,821],[872,282],[872,256],[872,476],[872,974],[754,637],[754,770],[754,811],[754,143],[754,629],[754,302],[754,771],[754,130],[754,169],[502,550],[502,314],[502,994],[502,787],[502,852],[502,808],[502,475],[741,548],[741,899],[741,766],[741,945],[741,921],[741,844],[741,225],[741,351],[741,941],[741,888],[2,988],[2,760],[2,770],[2,161],[2,500],[2,816],[2,225],[2,235],[2,987],[762,840],[762,842],[762,58],[762,965],[762,222],[762,496],[762,872],[762,524],[897,137],[897,952],[897,359],[897,797],[897,55],[897,189],[897,543],[897,950],[897,767],[219,524],[219,228],[219,903],[509,640],[509,498],[509,461],[509,258],[509,206],[509,406],[672,412],[672,75],[672,870],[672,801],[672,293],[672,496],[672,293],[672,458],[672,303],[672,194],[886,433],[886,771],[886,372],[886,156],[886,894],[886,16],[886,707],[886,20],[886,901],[886,527],[19,545],[19,57],[19,70],[19,177],[69,185],[69,374],[69,367],[69,182],[69,908],[69,436],[69,454],[69,427],[100,486],[100,976]]
so = Solution()
print(so.getOrder(tasks))