# Content routing card

```yaml
intent: create | update | merge | attach
content_type:
topic_or_project:
candidate_path:
existing_canonical_document:
why_this_location:
nearest_index:
source:
routing_confidence: high | medium | low
```

## Decision

- High confidence: write to the formal location.
- Medium confidence: inspect more context or ask one necessary question.
- Low confidence: keep it in Inbox with candidate destination and exit condition.

## Before creating

- [ ] Searched same topic, project, date, and document type.
- [ ] Confirmed no canonical document can absorb the change.
- [ ] Defined both an outgoing link and a navigation entry.
- [ ] Confirmed this is not a temporary output folder.
