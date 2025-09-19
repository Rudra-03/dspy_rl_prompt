"""Benchmark tasks for evaluating the DSPy RL optimization pipeline."""

from typing import List, Dict, Any
from dataclasses import dataclass
import json
import random

@dataclass
class BenchmarkTask:
    """Represents a benchmark task for evaluation."""
    name: str
    description: str
    category: str
    difficulty: str  # 'easy', 'medium', 'hard'
    base_instruction: str
    test_cases: List[Dict[str, Any]]
    success_criteria: List[str]
    target_metrics: List[str]

class BenchmarkSuite:
    """Collection of benchmark tasks for comprehensive evaluation."""
    
    def __init__(self):
        self.tasks = self._initialize_benchmark_tasks()
    
    def get_tasks_by_category(self, category: str) -> List[BenchmarkTask]:
        """Get all tasks in a specific category."""
        return [task for task in self.tasks if task.category == category]
    
    def get_tasks_by_difficulty(self, difficulty: str) -> List[BenchmarkTask]:
        """Get all tasks of a specific difficulty level."""
        return [task for task in self.tasks if task.difficulty == difficulty]
    
    def _initialize_benchmark_tasks(self) -> List[BenchmarkTask]:
        """Initialize the complete set of benchmark tasks."""
        
        tasks = []
        
        # Question Answering Tasks
        tasks.extend(self._create_qa_tasks())
        
        # Mathematical Problem Solving Tasks
        tasks.extend(self._create_math_tasks())
        
        # Text Analysis Tasks
        tasks.extend(self._create_text_analysis_tasks())
        
        # Logical Reasoning Tasks
        tasks.extend(self._create_reasoning_tasks())
        
        # Multi-step Workflow Tasks
        tasks.extend(self._create_workflow_tasks())
        
        return tasks
    
    def _create_qa_tasks(self) -> List[BenchmarkTask]:
        """Create question answering benchmark tasks."""
        
        tasks = []
        
        # Easy QA Task
        easy_qa = BenchmarkTask(
            name="basic_qa",
            description="Answer basic factual questions",
            category="question_answering",
            difficulty="easy",
            base_instruction="Answer the following question accurately.",
            test_cases=[
                {
                    'input': 'What is the capital of Japan?',
                    'expected_output': 'Tokyo',
                    'tools': {}
                },
                {
                    'input': 'How many days are in a leap year?',
                    'expected_output': '366',
                    'tools': {}
                },
                {
                    'input': 'What is the largest planet in our solar system?',
                    'expected_output': 'Jupiter',
                    'tools': {}
                },
                {
                    'input': 'Who painted the Mona Lisa?',
                    'expected_output': 'Leonardo da Vinci',
                    'tools': {}
                },
                {
                    'input': 'What is the chemical symbol for gold?',
                    'expected_output': 'Au',
                    'tools': {}
                }
            ],
            success_criteria=['Accuracy > 0.8', 'Concise answers', 'Factual correctness'],
            target_metrics=['accuracy', 'efficiency', 'confidence']
        )
        tasks.append(easy_qa)
        
        # Medium QA Task
        medium_qa = BenchmarkTask(
            name="contextual_qa",
            description="Answer questions requiring contextual understanding",
            category="question_answering",
            difficulty="medium",
            base_instruction="Read the context carefully and answer the question based on the information provided.",
            test_cases=[
                {
                    'input': 'Context: The Renaissance was a period of cultural rebirth in Europe from the 14th to 17th centuries. It began in Italy and spread throughout Europe. Question: Where did the Renaissance begin?',
                    'expected_output': 'Italy',
                    'tools': {}
                },
                {
                    'input': 'Context: Photosynthesis is the process by which plants convert sunlight, carbon dioxide, and water into glucose and oxygen. Question: What are the main inputs for photosynthesis?',
                    'expected_output': 'sunlight, carbon dioxide, and water',
                    'tools': {}
                },
                {
                    'input': 'Context: The Great Wall of China was built over many centuries by different dynasties. It stretches over 13,000 miles. Question: How long is the Great Wall of China?',
                    'expected_output': 'over 13,000 miles',
                    'tools': {}
                }
            ],
            success_criteria=['Context comprehension', 'Accurate extraction', 'Complete answers'],
            target_metrics=['accuracy', 'completeness', 'confidence']
        )
        tasks.append(medium_qa)
        
        return tasks
    
    def _create_math_tasks(self) -> List[BenchmarkTask]:
        """Create mathematical problem solving benchmark tasks."""
        
        tasks = []
        
        # Easy Math Task
        easy_math = BenchmarkTask(
            name="basic_arithmetic",
            description="Solve basic arithmetic problems",
            category="mathematics",
            difficulty="easy",
            base_instruction="Solve the mathematical problem and provide the numerical answer.",
            test_cases=[
                {
                    'input': '25 + 37 = ?',
                    'expected_output': '62',
                    'tools': {}
                },
                {
                    'input': '144 ÷ 12 = ?',
                    'expected_output': '12',
                    'tools': {}
                },
                {
                    'input': '8 × 7 = ?',
                    'expected_output': '56',
                    'tools': {}
                },
                {
                    'input': '100 - 23 = ?',
                    'expected_output': '77',
                    'tools': {}
                }
            ],
            success_criteria=['Correct calculation', 'Numerical accuracy', 'Clear presentation'],
            target_metrics=['accuracy', 'efficiency']
        )
        tasks.append(easy_math)
        
        # Medium Math Task
        medium_math = BenchmarkTask(
            name="word_problems",
            description="Solve mathematical word problems with multiple steps",
            category="mathematics",
            difficulty="medium",
            base_instruction="Read the problem carefully, identify the mathematical operations needed, and solve step by step.",
            test_cases=[
                {
                    'input': 'Sarah has 24 apples. She gives 1/3 of them to her friend and eats 2 apples herself. How many apples does she have left?',
                    'expected_output': '14',
                    'tools': {}
                },
                {
                    'input': 'A rectangle has a length of 15 cm and a width of 8 cm. What is its perimeter?',
                    'expected_output': '46 cm',
                    'tools': {}
                },
                {
                    'input': 'Tom buys 3 notebooks for $4.50 each and 2 pens for $1.25 each. How much does he spend in total?',
                    'expected_output': '$16.00',
                    'tools': {}
                }
            ],
            success_criteria=['Correct final answer', 'Logical problem breakdown', 'Proper units'],
            target_metrics=['accuracy', 'completeness', 'confidence']
        )
        tasks.append(medium_math)
        
        # Hard Math Task
        hard_math = BenchmarkTask(
            name="complex_problems",
            description="Solve complex multi-step mathematical problems",
            category="mathematics",
            difficulty="hard",
            base_instruction="Analyze the problem systematically, break it into steps, show your work clearly, and provide the final answer with proper justification.",
            test_cases=[
                {
                    'input': 'A company\'s profit increases by 15% each year. If the profit was $80,000 in 2020, what will it be in 2023?',
                    'expected_output': '$121,670',
                    'tools': {}
                },
                {
                    'input': 'Find the area of a triangle with vertices at (0,0), (4,0), and (2,3).',
                    'expected_output': '6 square units',
                    'tools': {}
                }
            ],
            success_criteria=['Mathematical accuracy', 'Clear methodology', 'Complete solution'],
            target_metrics=['accuracy', 'completeness', 'confidence']
        )
        tasks.append(hard_math)
        
        return tasks
    
    def _create_text_analysis_tasks(self) -> List[BenchmarkTask]:
        """Create text analysis benchmark tasks."""
        
        tasks = []
        
        # Easy Text Analysis
        easy_text = BenchmarkTask(
            name="sentiment_analysis",
            description="Determine the sentiment of given text",
            category="text_analysis",
            difficulty="easy",
            base_instruction="Analyze the sentiment of the given text and classify it as positive, negative, or neutral.",
            test_cases=[
                {
                    'input': 'I love this beautiful sunny day!',
                    'expected_output': 'positive',
                    'tools': {}
                },
                {
                    'input': 'This movie was terrible and boring.',
                    'expected_output': 'negative',
                    'tools': {}
                },
                {
                    'input': 'The weather is cloudy today.',
                    'expected_output': 'neutral',
                    'tools': {}
                },
                {
                    'input': 'Amazing performance by the team!',
                    'expected_output': 'positive',
                    'tools': {}
                }
            ],
            success_criteria=['Accurate classification', 'Consistent reasoning', 'Clear categorization'],
            target_metrics=['accuracy', 'confidence']
        )
        tasks.append(easy_text)
        
        # Medium Text Analysis
        medium_text = BenchmarkTask(
            name="text_summarization",
            description="Summarize longer texts while preserving key information",
            category="text_analysis",
            difficulty="medium",
            base_instruction="Read the text carefully and provide a concise summary that captures the main points.",
            test_cases=[
                {
                    'input': 'Artificial intelligence (AI) is transforming industries worldwide. From healthcare to finance, AI applications are improving efficiency and accuracy. Machine learning algorithms can analyze vast amounts of data to identify patterns and make predictions. However, ethical considerations around AI deployment remain important, including issues of bias, privacy, and job displacement.',
                    'expected_output': 'AI is transforming industries by improving efficiency and accuracy through machine learning and data analysis, but ethical concerns about bias, privacy, and job displacement must be addressed.',
                    'tools': {}
                },
                {
                    'input': 'Climate change is one of the most pressing challenges of our time. Rising global temperatures are causing sea levels to rise, weather patterns to change, and ecosystems to shift. Scientists agree that human activities, particularly greenhouse gas emissions, are the primary cause. Immediate action is needed to reduce emissions and adapt to changing conditions.',
                    'expected_output': 'Climate change, caused primarily by human greenhouse gas emissions, is leading to rising temperatures, sea level rise, and ecosystem changes, requiring immediate action for emissions reduction and adaptation.',
                    'tools': {}
                }
            ],
            success_criteria=['Key information preserved', 'Concise presentation', 'Logical flow'],
            target_metrics=['accuracy', 'completeness', 'efficiency']
        )
        tasks.append(medium_text)
        
        return tasks
    
    def _create_reasoning_tasks(self) -> List[BenchmarkTask]:
        """Create logical reasoning benchmark tasks."""
        
        tasks = []
        
        # Easy Reasoning
        easy_reasoning = BenchmarkTask(
            name="basic_logic",
            description="Solve basic logical reasoning problems",
            category="logical_reasoning",
            difficulty="easy",
            base_instruction="Use logical reasoning to solve the problem step by step.",
            test_cases=[
                {
                    'input': 'All birds can fly. Penguins are birds. Can penguins fly?',
                    'expected_output': 'Based on the given premises, yes, but in reality, penguins cannot fly.',
                    'tools': {}
                },
                {
                    'input': 'If it rains, the ground gets wet. The ground is wet. Did it rain?',
                    'expected_output': 'Not necessarily. The ground could be wet for other reasons.',
                    'tools': {}
                },
                {
                    'input': 'All cats are mammals. Fluffy is a cat. Is Fluffy a mammal?',
                    'expected_output': 'Yes, Fluffy is a mammal.',
                    'tools': {}
                }
            ],
            success_criteria=['Logical consistency', 'Clear reasoning', 'Correct conclusions'],
            target_metrics=['accuracy', 'completeness', 'confidence']
        )
        tasks.append(easy_reasoning)
        
        # Medium Reasoning
        medium_reasoning = BenchmarkTask(
            name="pattern_recognition",
            description="Identify patterns and solve sequence problems",
            category="logical_reasoning",
            difficulty="medium",
            base_instruction="Analyze the given sequence or pattern and determine what comes next.",
            test_cases=[
                {
                    'input': 'What comes next in this sequence: 2, 4, 8, 16, ?',
                    'expected_output': '32',
                    'tools': {}
                },
                {
                    'input': 'Complete the pattern: A, C, E, G, ?',
                    'expected_output': 'I',
                    'tools': {}
                },
                {
                    'input': 'What is the next number: 1, 1, 2, 3, 5, 8, ?',
                    'expected_output': '13',
                    'tools': {}
                }
            ],
            success_criteria=['Pattern identification', 'Correct prediction', 'Clear explanation'],
            target_metrics=['accuracy', 'completeness', 'confidence']
        )
        tasks.append(medium_reasoning)
        
        return tasks
    
    def _create_workflow_tasks(self) -> List[BenchmarkTask]:
        """Create multi-step workflow benchmark tasks."""
        
        tasks = []
        
        # Medium Workflow Task
        medium_workflow = BenchmarkTask(
            name="recipe_planning",
            description="Plan and organize cooking recipes with multiple steps",
            category="workflow_automation",
            difficulty="medium",
            base_instruction="Organize the cooking process into clear, sequential steps with proper timing and preparation.",
            test_cases=[
                {
                    'input': 'Create a step-by-step plan for making spaghetti with tomato sauce. Include: boiling pasta (10 min), making sauce (15 min), and combining them.',
                    'expected_output': '1. Start heating water for pasta 2. While water heats, prepare sauce ingredients 3. Begin cooking sauce (15 min) 4. Add pasta to boiling water (10 min) 5. Drain pasta when sauce is nearly done 6. Combine pasta and sauce 7. Serve immediately',
                    'tools': {}
                },
                {
                    'input': 'Plan a morning routine that includes: shower (15 min), breakfast (10 min), getting dressed (5 min), and commute (20 min). Total time available: 60 minutes.',
                    'expected_output': '1. Shower (15 min) 2. Get dressed (5 min) 3. Prepare and eat breakfast (10 min) 4. Leave for commute (20 min) - Total: 50 minutes with 10 minutes buffer',
                    'tools': {}
                }
            ],
            success_criteria=['Logical sequence', 'Time management', 'Practical organization'],
            target_metrics=['completeness', 'efficiency', 'confidence']
        )
        tasks.append(medium_workflow)
        
        # Hard Workflow Task
        hard_workflow = BenchmarkTask(
            name="project_management",
            description="Create complex project plans with dependencies and resource allocation",
            category="workflow_automation",
            difficulty="hard",
            base_instruction="Analyze the project requirements, identify dependencies, allocate resources efficiently, and create a detailed execution plan.",
            test_cases=[
                {
                    'input': 'Plan a website development project with these tasks: Design (5 days), Frontend development (8 days), Backend development (10 days), Testing (3 days), Deployment (1 day). Frontend depends on design, backend can start anytime, testing depends on both frontend and backend completion.',
                    'expected_output': 'Week 1: Start Design (5 days) and Backend development (10 days) in parallel. Week 2: Complete Design, start Frontend development (8 days). Week 3: Complete Backend and Frontend. Week 4: Testing (3 days) then Deployment (1 day). Total: 18 days with parallel execution.',
                    'tools': {}
                }
            ],
            success_criteria=['Dependency management', 'Resource optimization', 'Realistic timeline'],
            target_metrics=['completeness', 'efficiency', 'accuracy']
        )
        tasks.append(hard_workflow)
        
        return tasks

def run_benchmark_evaluation(pipeline, task_names: List[str] = None) -> Dict[str, Any]:
    """
    Run benchmark evaluation on specified tasks.
    
    Args:
        pipeline: The DSPy RL pipeline to evaluate
        task_names: List of specific task names to run (None for all tasks)
        
    Returns:
        Dictionary containing benchmark results
    """
    
    benchmark_suite = BenchmarkSuite()
    
    if task_names:
        tasks_to_run = [task for task in benchmark_suite.tasks if task.name in task_names]
    else:
        tasks_to_run = benchmark_suite.tasks
    
    results = {
        'benchmark_summary': {
            'total_tasks': len(tasks_to_run),
            'categories': list(set(task.category for task in tasks_to_run)),
            'difficulties': list(set(task.difficulty for task in tasks_to_run))
        },
        'task_results': {},
        'category_performance': {},
        'difficulty_performance': {},
        'overall_metrics': {}
    }
    
    print(f"🧪 Running benchmark evaluation on {len(tasks_to_run)} tasks...")
    
    # Convert benchmark tasks to optimization tasks
    from main import OptimizationTask
    
    all_performances = []
    category_performances = {}
    difficulty_performances = {}
    
    for benchmark_task in tasks_to_run:
        print(f"\n📋 Evaluating: {benchmark_task.name}")
        
        # Convert to OptimizationTask format
        optimization_task = OptimizationTask(
            task_id=benchmark_task.name,
            task_description=benchmark_task.description,
            base_instruction=benchmark_task.base_instruction,
            evaluation_data=benchmark_task.test_cases,
            success_criteria=benchmark_task.success_criteria,
            target_metrics=benchmark_task.target_metrics,
            optimization_methods=['gepa', 'miprov2']  # Use faster methods for benchmarking
        )
        
        # Run optimization
        task_result = pipeline.run_optimization_pipeline(optimization_task)
        
        # Store results
        results['task_results'][benchmark_task.name] = {
            'category': benchmark_task.category,
            'difficulty': benchmark_task.difficulty,
            'base_performance': task_result['base_performance']['metrics']['overall_score'],
            'best_performance': task_result['best_performance'],
            'improvement': task_result['best_performance'] - task_result['base_performance']['metrics']['overall_score'],
            'best_method': task_result.get('best_method', 'None')
        }
        
        # Aggregate by category
        if benchmark_task.category not in category_performances:
            category_performances[benchmark_task.category] = []
        category_performances[benchmark_task.category].append(task_result['best_performance'])
        
        # Aggregate by difficulty
        if benchmark_task.difficulty not in difficulty_performances:
            difficulty_performances[benchmark_task.difficulty] = []
        difficulty_performances[benchmark_task.difficulty].append(task_result['best_performance'])
        
        all_performances.append(task_result['best_performance'])
    
    # Calculate category averages
    for category, performances in category_performances.items():
        results['category_performance'][category] = {
            'average_performance': sum(performances) / len(performances),
            'best_performance': max(performances),
            'task_count': len(performances)
        }
    
    # Calculate difficulty averages
    for difficulty, performances in difficulty_performances.items():
        results['difficulty_performance'][difficulty] = {
            'average_performance': sum(performances) / len(performances),
            'best_performance': max(performances),
            'task_count': len(performances)
        }
    
    # Overall metrics
    if all_performances:
        results['overall_metrics'] = {
            'average_performance': sum(all_performances) / len(all_performances),
            'best_performance': max(all_performances),
            'worst_performance': min(all_performances),
            'performance_std': (sum((p - sum(all_performances)/len(all_performances))**2 for p in all_performances) / len(all_performances))**0.5
        }
    
    return results

# Example usage
if __name__ == "__main__":
    # Create and display benchmark suite
    suite = BenchmarkSuite()
    
    print("📊 Benchmark Suite Overview")
    print("=" * 40)
    
    categories = {}
    difficulties = {}
    
    for task in suite.tasks:
        if task.category not in categories:
            categories[task.category] = 0
        categories[task.category] += 1
        
        if task.difficulty not in difficulties:
            difficulties[task.difficulty] = 0
        difficulties[task.difficulty] += 1
    
    print(f"Total Tasks: {len(suite.tasks)}")
    print("\nBy Category:")
    for category, count in categories.items():
        print(f"  {category}: {count} tasks")
    
    print("\nBy Difficulty:")
    for difficulty, count in difficulties.items():
        print(f"  {difficulty}: {count} tasks")
    
    print("\nTask Details:")
    for task in suite.tasks:
        print(f"  {task.name} ({task.category}, {task.difficulty}): {len(task.test_cases)} test cases")
