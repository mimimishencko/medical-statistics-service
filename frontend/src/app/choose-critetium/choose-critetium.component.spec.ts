import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ChooseCritetiumComponent } from './choose-critetium.component';

describe('ChooseCritetiumComponent', () => {
  let component: ChooseCritetiumComponent;
  let fixture: ComponentFixture<ChooseCritetiumComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ChooseCritetiumComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ChooseCritetiumComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
