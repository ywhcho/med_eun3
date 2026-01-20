from django.core.management.base import BaseCommand
from medicine.models import Medicine

class Command(BaseCommand):
    help = '의약품 샘플 데이터 생성'

    def handle(self, *args, **kwargs):
        # 기존 데이터 확인
        if Medicine.objects.count() > 0:
            self.stdout.write(self.style.WARNING('이미 데이터가 존재합니다.'))
            return

        medicines = [
            {
                'drug_name': '타이레놀정',
                'ingredient': '아세트아미노펜',
                'efficacy': '해열, 진통(두통, 치통, 생리통 등)',
                'dosage': '성인: 1회 1-2정, 1일 3-4회 복용',
                'precautions': '간 질환자 주의, 알코올과 함께 복용 금지',
                'company': '한국얀센'
            },
            {
                'drug_name': '게보린정',
                'ingredient': '아세트아미노펜, 에텐자미드',
                'efficacy': '두통, 치통, 발열, 근육통 등의 진통 및 해열',
                'dosage': '성인: 1회 1정, 1일 3회 복용',
                'precautions': '위장장애가 있을 수 있으며, 카페인 함유',
                'company': '삼진제약'
            },
            {
                'drug_name': '베아제정',
                'ingredient': '디아스타제, 펩신',
                'efficacy': '소화불량, 식욕부진, 과식 등으로 인한 소화장애 개선',
                'dosage': '성인: 1회 2정, 1일 3회 식후 복용',
                'precautions': '임산부는 복용 전 의사와 상담',
                'company': '종근당'
            },
            {
                'drug_name': '훼스탈플러스정',
                'ingredient': '판크레아틴, 셀룰라제',
                'efficacy': '소화불량, 식욕감퇴, 과식, 체함 등',
                'dosage': '성인: 1회 1-2정, 1일 3회 식후 복용',
                'precautions': '급성 췌장염 환자 복용 금지',
                'company': '동아제약'
            },
            {
                'drug_name': '아스피린프로텍트',
                'ingredient': '아스피린',
                'efficacy': '혈전 생성 억제, 뇌졸중 및 심근경색 예방',
                'dosage': '성인: 1일 1회 100mg 복용',
                'precautions': '출혈 경향이 있는 환자 주의, 위장장애 가능',
                'company': '바이엘코리아'
            },
            {
                'drug_name': '부루펜정',
                'ingredient': '이부프로펜',
                'efficacy': '소염, 진통, 해열(두통, 치통, 근육통, 생리통 등)',
                'dosage': '성인: 1회 200-400mg, 1일 3-4회 복용',
                'precautions': '위장장애, 소화성 궤양 환자 주의',
                'company': '삼일제약'
            },
            {
                'drug_name': '판피린티정',
                'ingredient': '아세트아미노펜, 이소프로필안티피린',
                'efficacy': '감기의 제 증상(두통, 발열, 근육통) 완화',
                'dosage': '성인: 1회 1정, 1일 3회 복용',
                'precautions': '운전 및 기계조작 시 주의, 졸음 유발 가능',
                'company': '동화약품'
            },
            {
                'drug_name': '지르텍정',
                'ingredient': '세티리진',
                'efficacy': '알레르기성 비염, 두드러기, 가려움증',
                'dosage': '성인: 1일 1회 1정 복용',
                'precautions': '졸음을 유발할 수 있으므로 운전 시 주의',
                'company': '유씨비코리아'
            },
            {
                'drug_name': '알레그라정',
                'ingredient': '펙소페나딘',
                'efficacy': '알레르기성 비염, 만성 두드러기',
                'dosage': '성인: 1일 2회 1정 복용',
                'precautions': '졸음이 적으나 개인차가 있을 수 있음',
                'company': '사노피아벤티스'
            },
            {
                'drug_name': '박카스F정',
                'ingredient': '타우린, 카페인, 이노시톨',
                'efficacy': '육체 피로 회복, 영양 보급',
                'dosage': '성인: 1일 1회 1정 복용',
                'precautions': '카페인 함유로 불면증 주의',
                'company': '동아제약'
            },
            {
                'drug_name': '우루사정',
                'ingredient': '우르소데옥시콜산',
                'efficacy': '간기능 개선, 담즙 분비 촉진, 소화 불량',
                'dosage': '성인: 1회 1정, 1일 3회 식후 복용',
                'precautions': '담도 폐쇄 환자 복용 금지',
                'company': '대웅제약'
            },
            {
                'drug_name': '레바미피드정',
                'ingredient': '레바미피드',
                'efficacy': '위염, 위궤양 치료 및 개선',
                'dosage': '성인: 1회 100mg, 1일 3회 식후 복용',
                'precautions': '임부 복용 주의, 드물게 발진 가능',
                'company': '한미약품'
            },
            {
                'drug_name': '에어탈정',
                'ingredient': '아세클로페낙',
                'efficacy': '관절염, 근육통, 염좌 등의 소염 및 진통',
                'dosage': '성인: 1회 1정, 1일 2회 복용',
                'precautions': '위장장애, 심혈관계 질환자 주의',
                'company': '대웅제약'
            },
            {
                'drug_name': '가스모틴정',
                'ingredient': '모사프리드',
                'efficacy': '위장관 운동 촉진, 소화불량, 구토',
                'dosage': '성인: 1회 1정, 1일 3회 식전 복용',
                'precautions': '임산부, 수유부 복용 주의',
                'company': '대웅제약'
            },
            {
                'drug_name': '탁센정',
                'ingredient': '세파클러',
                'efficacy': '세균 감염증 치료(기관지염, 편도염, 방광염 등)',
                'dosage': '성인: 1회 250mg, 1일 3회 복용',
                'precautions': '페니실린 알레르기 환자 주의',
                'company': '한독약품'
            }
        ]

        for medicine_data in medicines:
            Medicine.objects.create(**medicine_data)
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {len(medicines)} medicines'))
